"use strict";
console.log("i am saving tracking!");

function saveTracking(evt) {
    console.log('hello saved tracking');

    evt.preventDefault();

    let today = new Date();
    let date = (today.getMonth()+1)+'-'+today.getDate()+'-'+today.getFullYear();
    let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    const child = $('#notes').data();
    let child_id = child.child_id;

    let url = "/save-tracking";
    let savedData = {
                    //  'search_queries': query_terms,
                     'child_id': child_id,
                     'notes': $('#notes').val(),
                     'date': date,
                     'time': time,

                    };
    
    console.log(savedData['child_id']);
    console.log(savedData['date']);
    console.log(savedData['time']);
    console.log(savedData['notes']);

    $.get(url, savedData, (response) => {

        console.log(response);
        // let session[table_info] = {"tracking_id": response.tracking_id,
        //                           "date_time": response.date_time,
        //                           "search_queries": response.search_queries,
        //                           "note": response.note
        //                           }

        $('#tracking-id').html(table_info[tracking_id]);
        $('#date_time').html(table_info[date_time]);
        $('#search_queries').html(table_info[search_queries]);
        $('#notes').html(table_info[notes]);
        $('#notes').data('child');
    });
}

// This is happening after the elements are loaded on the page in tracking.js and child_bio instead
// $("#save-search").on("click", saveTracking);
