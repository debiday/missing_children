"use strict";
console.log("i am saving tracking!");

function saveTracking(evt) {
    console.log('hello saved tracking');

    evt.preventDefault();

    // Get date
    let today = new Date();
    let date = (today.getMonth()+1)+'-'+today.getDate()+'-'+today.getFullYear();
    let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

    //Get child_id
    let child = $('#notes').data();
    let child_id = child.child_id;

    //Get email
    let email = $('#user-email').text()

    //Get user_id
    let user_id = $('#user-id').text()


    let url = "/save-tracking";
    //saves values from the front end and sends it to server
    let savedData = {
                     'user_id': user_id,
                     'child_id': child_id,
                     'notes': $('#notes').val(),
                     'date': date,
                     'time': time,
                    //  'email': email
                    };

    console.log("**********")
    console.log(user_id)
    console.log(savedData['child_id']);
    console.log(savedData['date']);
    console.log(savedData['time']);
    console.log(savedData['notes']);

    $.post(url, savedData, (response) => {

        console.log(response);
        // let session[table_info] = {"tracking_id": response.tracking_id,
        //                           "date_time": response.date_time,
        //                           "search_queries": response.search_queries,
        //                           "note": response.note
        //                           }
        //add visually to html/ incrementing tables?

        // $('#tracking-id').html(table_info[tracking_id]);
        // $('#date_time').html(table_info[date_time]);
        // $('#search_queries').html(table_info[search_queries]);
        // $('#notes').html(table_info[notes]);
        // $('#notes').data('child');
    
    });
}

// This is happening after the elements are loaded on the page in tracking.js and child_bio instead
// $("#save-search").on("click", saveTracking);
