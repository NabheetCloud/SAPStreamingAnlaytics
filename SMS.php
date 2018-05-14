<?php
$request = file_get_contents('php://input');
$json= json_decode($request);
var_dump($json);
// Send SMS API$context = array();

$ch1 = curl_init('https://sandbox.api.sap.com/proximusenco/sms/outboundmessages');
$request_headers = array();
$request_headers[] = 'Content-Type: application/json';
$request_headers[] = 'Accept: application/json';
$request_headers[] = 'APIKey: <API Key>';
curl_setopt($ch1, CURLOPT_HTTPHEADER, $request_headers );
curl_setopt($ch1, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($ch1, CURLOPT_VERBOSE, 1);
curl_setopt($ch1, CURLOPT_HEADER, 1);
$context["message"] = "High RAM usage detected on Laptop";
$context["binary"] = false;
$context["destinations"] = ['+9111111111'];
var_dump($context);
curl_setopt($ch1, CURLOPT_POSTFIELDS,json_encode($context)           );
$resp = curl_exec($ch1);
curl_close($ch1);

?>