/**
 * Script that updates the text color of the <header>
 * element to red (#FF0000) when the user clicks on the
 * DIV tag with ID red_header:
 */
$('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
});
