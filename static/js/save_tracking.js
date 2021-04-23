"use strict";
console.log("i am saving tracking!");

function saveTracking(evt) {
    console.log('hello saved tracking');

    evt.preventDefault();

    
    let url = "/save-tracking";
    let savedData = {'tracking_id': tracking_id,
                     'date_time': date_time,
                     'search_queries': search_queries,
                     'notes': notes
                    };

    $.get(url, savedData, (response) => {

        console.log(response);
        let table_info = {"tracking_id": response.tracking_id,
                          "date_time": response.date_time,
                          "search_queries": response.search_queries,
                          "notes": response.notes
                        }

        $('#tracking-id').html(table_info[tracking_id]);
        $('#date_time').html(table_info[date_time]);
        $('#search_queries').html(table_info[search_queries]);
        $('#notes').html(table_info[notes]);
        
    });
}

// This is happening after the elements are loaded on the page in tracking.js and child_bio instead
// $("#save-search").on("click", saveTracking);
