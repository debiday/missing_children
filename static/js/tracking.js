"use strict";


function showSearchResult(evt) {
    console.log('hello tracking');

    evt.preventDefault();

    
    let url = "/search.json";
    let childData = {'fname': $('#fname').val(),
                     'lname': $('#lname').val(),
                    'county':  $('#county').val(),
                    'state':  $('#state').val(),
                    'missing_age':  $('#missing_age').val(),
                    'age_2021':  $('#age_2021').val(),
                    'date_missing':  $('#date_missing').val()
    };

    $.post(url, childData, (response) => {

        console.log(response);

        // To find sum of children in list
        const children = response.split(",");
        
        // To format the children data in the list
        console.log(children)
        console.log(children.length)
        let total_results = children.length - 1
        // for loop through response (list of child objects), display certain attributes (ex: first name)
        // when displaying first name, use href and link to a new server route
        // this new server route should display child's information

        // const children = [];
        $('#result_num').html(total_results);
        $('#results').html(response);
    });
}



// $('#tracking-form-test').on('submit', (evt) => {
//     evt.preventDefault();

//     const childFormInputs = {'fname': $('#fname').val(),
//                             'lname': $('#lname').val(),
//                             'county':  $('#county').val(),
//                             'state':  $('#state').val(),
//                             'missing_age':  $('#missing_age').val(),
//                             'age_2021':  $('#age_2021').val(),
//                             'date_missing':  $('#date_missing').val()
//     };

//     $.post('/search.json', childFormInputs, (res) => {
//         console.log("**************")
//         console.log(res)

//         $('#results').html(res);
// });
// })










$("#tracking-form").on("submit", showSearchResult);
//$("#find-button").on("submit", showSameAge);