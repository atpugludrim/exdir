#!/usr/bin/perl

use LWP::Simple;
$contents = get("http://wttr.in/28.545031683577257,77.19041434469378?format=%t %h");
#($tmp, $rh) = ($contents =~ m/([-|\+]\d+)/g);
($tmp, $rh) = ($contents =~ m/([-|\+][\d.]+).*\s+([\d.]+)%/g);
$tmp = $tmp * 1;
$rh = $rh * 1;
$a = 17.625;
$b = 243.04;
sub f{
    $a = 17.625;
    $b = 243.04;
    $T = $_[0];
    $RH = $_[1];
    return (log($RH/100) + $a * $T / ($b + $T));
}
$td = $b * f($tmp,$rh) / ($a - f($tmp,$rh));
$contents = get("https://wttr.in/28.545031683577257,77.19041434469378?format=%C %t (%f) %h %p %w");
print "Content-Type:text/html\r\n\r\n";
print '<html><body><h3>';
printf "IIT Delhi: %s %.2f\n", $contents, $td;
print '</h3></body></html>';
