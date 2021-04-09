"use strict";
print("*****")
print(age)
function showSameAge(evt) {
    evt.preventDefault();

    let url= "/age.json";
    let ageData = {"age": $("#user-age").val()};

    $.get(url, ageData, (response) => {
        $('#child-info').html(response.fname);
    });
}

$("#age_form").on("submit", showSameAge);