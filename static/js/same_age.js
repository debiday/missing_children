"use strict";
console.log('hello');

function showSameAge(evt) {
    console.log("HI");
    evt.preventDefault();

    
    let url="/age";
    let ageData = {"age": $("#user-age").val()};


    $.get(url, ageData, (response) => {

        console.log(response);
        // const children = [];

        $('#child-info').html(response);
    });
}

$("#find-button").on("click", showSameAge);