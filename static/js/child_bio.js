"use strict";
console.log("hello bio");

function showBioResult(evt) {
    console.log('hello tracking');

    evt.preventDefault();

    
    let url = "/child_bio";
    let childData = {'child_id': evt.target.id};
    console.log(childData);

    $.post(url, childData, (response) => {

        console.log(response.child_id);
        let child_info = {"fname": response.fname,
                          "lname": response.lname,
                          "date_missing": response.date_missing,
                          "missing_age": response.missing_age,
                          "age_2021": response.age_2021,
                          "city": response.city,
                          "county": response.county,
                          "state": response.state
                        }

        let all_info = `Name: ${child_info.fname} ${child_info.lname}\n`+ 
                        `Date Missing: ${child_info.date_missing}\n`+
                        `Age Missing: ${child_info.missing_age}\n`+
                        `Current Age: ${child_info.age_2021}\n`+
                        `City: ${child_info.city}\n`+
                        `County: ${child_info.county}\n`+
                        `State: ${child_info.state}\n`+
                        `Notes: `

        // let all_info = response.state

        $('#notes').data(childData);
        $('#notes').html(all_info);
    });
}

// This is happening after the elements are loaded on the page in tracking.js instead
// $(".child_bio").on("click", showBioResult);