/**
 * Script that fetches the character name from the URL:
 * https://swapi-api.hbtn.io/api/people/5/?format=json
 */
$.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: result => {
        $('DIV#character').text(result.name);
    }
});
