{% load staticfiles %}

$( function() {
    $( "#datepicker" ).datepicker({
        showButtonPanel: true,
        showOtherMonths: true,
        selectOtherMonths: true,
        formatDate: "dd-mm-yy",
        minDate: 0
        showOn: "button",
        buttonImage: "images/calendar_small.png",
        //buttonImage: "{% static 'images/calendar_small.png' %}",
        buttonImageOnly: true,
        buttonText: "Select date"
    });

    //$( "#datepicker" ).datepicker.formatDate( "dd-mm-yy", $( this ).val() );
} );
alert("External js is working!");
$( function() {
    $( "input" ).checkboxradio();
} );

function urlToClipboard() {
  /* Get the text field */
  var copyText = document.URL;
  /* Select the text field */
  copyText.select();
  /* Copy the text inside the text field */
  document.execCommand("Copy");
  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}


