/**
 * Script that adds the class red to the <header>
 * element when the user clicks on the DIV tag with ID red_header
 */
$('DIV#red_header').click(() => {
    $('header').addClass('red');
});
