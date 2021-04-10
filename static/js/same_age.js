"use strict";
console.log('hello');

function showSameAge(evt) {
    console.log('hello');

    evt.preventDefault();

    
    let url="/age";
    let ageData = {"user-age": $("#user-age").val()};


    $.get(url, ageData, (response) => {

        console.log(response);
        // const children = [];

        $('#child-info').html(response);
    });
}
$("#age-form").on("submit", showSameAge);
//$("#find-button").on("submit", showSameAge);