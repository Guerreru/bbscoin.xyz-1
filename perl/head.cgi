#!/usr/bin/perl

if ($IN_HOME) {
print <<"HTML";
<!DOCTYPE html>
<html lang="$lang->{'html_lang'}" dir="$lang->{'html_dir'}">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="$lang->{'description'}">
    <meta name="author" content="BBSCoin">
	<meta name="keywords" content="$lang->{'keywords'}" />

    <title>BBSCoin$subtitle</title>

    <base href="/" />

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom fonts for this template -->
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>

    <!-- Plugin CSS -->
    <link href="vendor/magnific-popup/magnific-popup.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/creative.min.css" rel="stylesheet">
    
	<!-- twitter card -->
	<meta property="twitter:url" content="https://bbscoin.xyz"/>
	<meta property="twitter:title" content="$lang->{'twitter_title'}"/>
	<meta property="twitter:description" content="$lang->{'description'}"/>
	<meta property="twitter:image" content="https://bbscoin.xyz/img/logos/bbscoin.png"/>

	<!-- favicon -->
	<link href="img/logos/favicon.ico" rel="shortcut icon">

  </head>
  <body id="page-top">
HTML
}
return 1;