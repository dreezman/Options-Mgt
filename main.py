








def readoptionfile():

    $myFile = "codes.txt";
    $fh = fopen($myFile, 'r');
    $theData = fread($fh, filesize($myFile));
    $assoc_array = array()
    $my_array = explode("\n", $theData);
    foreach($my_array as $line)
    {
    $tmp = explode(" ", $line);
    $assoc_array[$tmp[0]] = $tmp[1];
    }
    fclose($fh)

    // well
    the
    op
    wants
    the
    results
    to
    be in $codes
    $codes = $assoc_array;


// ========================= MAIN =======================

x NoneType ;
x,y Int;


print 'hello world!'

