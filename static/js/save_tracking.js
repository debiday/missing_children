"use strict";
console.log("i am saving tracking!");

function saveTracking(evt) {
    console.log('hello saved tracking');

    evt.preventDefault();

    
    let url = "/save-tracking";
    let savedData = {
                    //  'search_queries': query_terms,
                     'note': note
                    };
    console.log(savedData[search_queries]);
    $.get(url, savedData, (response) => {

        console.log(response);
        let session[table_info] = {"tracking_id": response.tracking_id,
                                  "date_time": response.date_time,
                                  "search_queries": response.search_queries,
                                  "note": response.note
                                  }

        $('#tracking-id').html(table_info[tracking_id]);
        $('#date_time').html(table_info[date_time]);
        $('#search_queries').html(table_info[search_queries]);
        $('#notes').html(table_info[notes]);
        $('#notes').data('child');
    });
}

// This is happening after the elements are loaded on the page in tracking.js and child_bio instead
// $("#save-search").on("click", saveTracking);
