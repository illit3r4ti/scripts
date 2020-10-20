<?

// MODIFIED FUNCTION TO DERIVE KEY FROM CIPHERTEXT ^ PLAINTEXT

// $defaultdata = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
// $ciphertext = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");

// function xor_encrypt($ciphertext, $defaultdata) {
//     // $key = '<censored>';
//     $text = $ciphertext;
//     $outText = '';

//     // Iterate through each character
//     for($i=0;$i<strlen($ciphertext);$i++) {
//     $outText .= $ciphertext[$i] ^ $defaultdata[$i % strlen($defaultdata)];
//     }

//     return $outText;
// }

// $key = xor_encrypt($ciphertext,$defaultdata);

// echo $key

// ORIGINAL FUNCTION W/KEY AND SHOWPASSWORD VAL ALTERED

$defaultdata = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

echo base64_encode(xor_encrypt($defaultdata));

?>