/**
 * Script that adds a <li> element to a list
 * when the user clicks on the DIV tag with ID add_item
 */
$('DIV#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
});
