"use strict";


function showSameAge(evt) {
    console.log('hello');

    evt.preventDefault();

    
    let url="/age";
    let ageData = {"user-age": $("#user-age").val()};


    $.get(url, ageData, (response) => {

        console.log(response);
        // const children = [];
        response = "<b>Children the same age as you in 2021 are:<b><br>" + "<br><h5><b>" + response + "<b></h5><br><br>Based on NAMUS database launched in 2007. Accessed April 2021";

        $('#child-info').html(response);
    });
}
$("#age-form").on("submit", showSameAge);
//$("#find-button").on("submit", showSameAge);