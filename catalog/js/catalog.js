$( document ).ready(function() {
    $.ajax({
        url: "/api/books",
        data: {},
        type: "GET",
        dataType: "json",
    })
    .done(function( json ) {
        $.each( json, function( arrayId, value ) {
            $( "#books" ).append(
                $( "<div/>", { "id": value._id, "class": "book pure-u-1-2" }).append(
                    $( "<p/>", { "class": "title", text: value.title })
                ).append(
                    $( "<img/>", { "class": "coverflow", "src": value.cover })
                )
            )
        });
        $( "div.book" ).click(function( event ) {
            $.ajax({
                url: "/api/books/" + this.id,
                data: {},
                type: "GET",
                dataType: "json",
            })
            .done(function ( json ) {
                $( "#details" ).empty();
                $( "#details" ).append(
                    $( "<div/>", { "class": "book-details" })
                );
                $.each( json, function ( k, v ) {
                    if ( k === "_id" ){ return }
                    if ( k === "cover" ) {
                        $( "#details" ).append(
                            $( "<img/>", { "class": "cover", "src": v })
                        )
                        return
                    }
                    $( "#details" ).append(
                        $( "<p/>", { "class": k, text: v })
                    )
                })
            }); 
        });
    })
    .fail(function( xhr, status, errorThrown ) {
        alert ("Sorry, there was a problem!" );
        console.log( "Error: " + errorThrown );
        console.log( "status: " + status );
        console.dir( xhr );
    });
});
