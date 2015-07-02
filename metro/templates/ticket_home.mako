<html>
<head>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.js"></script>
    <script src="http://malsup.github.com/jquery.form.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>

    <script>
        // AJAX for posting
        function create_post(form_submit_data) {
            console.log("create post is working!") // sanity check
            $.ajax({
                url: "ticket", // the endpoint
                type: "POST", // http method
                data: form_submit_data, // data sent with the post request

                // handle a successful response
                success: function (json_response) {
                    $('#post-text').val(''); // remove the value from the input
                    console.log(json_response); // log the returned json to the console
                    console.log("success"); // another sanity check

                    if (json_response.status==='success') {
                        //$('#ticket_price').text("The ticket amount is " + json_response.amount);
                        $('#ticket_message_success').html(json_response.message);
                        $('#ticket_success').show();
                    }
                    else {
                        $('#ticket_message_failure').text(json_response.message);
                        $('#ticket_failure').show();
                    }

                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    $('#ticket_message_failure').text("Unable to reach our servers this time.. :( ");
                    $('#ticket_failure').show();

                }
            });
        };
        function hide_and_clear_ticket_details(){
            $('.ticket_output').hide()
            $('#ticket_price').text("")
            $('#ticket_message').text("")
        }


        var availableTags = [
            "CST",
            "Masjid",
            "Sandhurst Road",
            "Byculla",
            "Chinchpokli",
            "Currey Road",
            "Parel",
            "Dadar",
            "Matunga",
            "Sion",
            "Kurla",
            "Vidyavihar",
            "Ghatkopar",
            "Vikhroli",
            "Kanjurmarg",
            "Bhandup",
            "Nahur",
            "Mulund",
            "Thane",
            "Kalyan"
        ];
        // wait for the DOM to be loaded
        $(document).ready(function () {

            $(".station").autocomplete({
                source: availableTags
            });
            
            // Submit post on submit
            $('#ticket_form').on('submit', function(event){
                event.preventDefault();
                console.log("form submitted!")  // sanity check
                var form_submit_data = $(this).serializeArray();
                create_post(form_submit_data);
            });

            $(".station").on('change', function(event){hide_and_clear_ticket_details()});

        });

    </script>
</head>
<body>
<form id="ticket_form" action="ticket" method="post">
    Starting Station: <input id = "start_station" class="station" type="text" name="start_station" />
    Ending Station: <input  id = "end_station" class="station" type="text" name="end_station" />
    <input type="submit" value="Get Ticket" />
</form>
<div class = "ticket_output" id="ticket_success" hidden="true">
    <p id="ticket_price"></p>
    <div id="ticket_message_success"></div>
    <p id="ticket_status"></p>
</div>
<div class = "ticket_output" id="ticket_failure" hidden="true">
    <p id="ticket_message_failure"></p>
</div>
</body>