function slugify(string) {
  return string
    .toString()
    .trim()
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w\-]+/g, "")
    .replace(/\-\-+/g, "-")
    .replace(/^-+/, "")
    .replace(/-+$/, "");
}

function delete_place(div_id){
    var el = document.getElementById(div_id);
    el.parentNode.removeChild(el);
}

function get_minus_btn(par_id){
    var btn = document.createElement('button');
    btn.className = "ui-button ui-widget ui-corner-all ui-button-icon-only";
    btn.id = par_id+"-minus";
    btn.title = "Delete this place";
    btn.addEventListener("click", function() {delete_place(par_id);});
    btn.type = "button";
    btn.innerHTML = '<span class="ui-icon ui-icon-minus"></span>';
    return btn;
}

function add_plc_str(plc_name){
    var vl = document.getElementById('plcs_str').value + plc_name + ",,";
    document.getElementById('plcs_str').setAttribute('value', vl);
}

function add_sub_place(plc_name) {
    var id = "sub_plc-"+slugify(plc_name);
    if (document.getElementById(id)) {
        alert(plc_name + " already added");
    } else{
        var newPlc = document.createElement('div');
        newPlc.id = id;
        newPlc.innerHTML = plc_name;
        newPlc.style.width = "40em";
        newPlc.appendChild(get_minus_btn(id));
        document.getElementById('added_plcs').appendChild(newPlc);
        add_plc_str(plc_name);
    }
}

//alert(configuration['pubway']['places']['QMU'])

/*$(function () {
    $('#id_sub_time').datetimepicker();
});*/

$( function() {
    $( "#id_sub_date" ).datepicker({
        showButtonPanel: true,
        showOtherMonths: true,
        selectOtherMonths: true,
        dateFormat: "dd/mm/yy",
        minDate: 0,
        showOn: "both",
        buttonImage: "/static/images/calendar_small.png",
        buttonImageOnly: true,
        buttonText: "Select date",
        changeMonth: true,
        changeYear: true
    });
} );

$( function() {
    $( "#sortable" ).sortable({
        connectWith: "#sortable",
        cancel: ".ui-state-disabled .portlet-toggle",
        handle: ".portlet-header",
        placeholder: "portlet-placeholder ui-corner-all"
    });
    $( "#sortable" ).disableSelection();
    $( ".portlet" )
        .addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
        .find( ".portlet-header" )
        .addClass( "ui-widget-header ui-corner-all" )
        .prepend( "<span class='ui-icon ui-icon-plusthick portlet-toggle'></span>");

    $( ".portlet-toggle" ).on( "click", function() {
        var icon = $( this );
        icon.toggleClass( "ui-icon-minusthick ui-icon-plusthick" );
        icon.closest( ".portlet" ).find( ".portlet-content" ).toggle();
    });
} );


$( function() {
$.widget( "custom.combobox", {
  _create: function() {
    this.wrapper = $( "<span>" )
      .addClass( "custom-combobox" )
      .insertAfter( this.element );

    this.element.hide();
    this._createAutocomplete();
    this._createShowAllButton();
  },

  _createAutocomplete: function() {
    var selected = this.element.children( ":selected" ),
      value = selected.val() ? selected.text() : "";

    this.input = $( "<input>" )
      .appendTo( this.wrapper )
      .val( value )
      .attr( "title", "" )
      .addClass( "custom-combobox-input ui-widget ui-widget-content ui-state-default ui-corner-left" )
      .autocomplete({
        delay: 0,
        minLength: 0,
        source: $.proxy( this, "_source" )
      })
      .tooltip({
        classes: {
          "ui-tooltip": "ui-state-highlight"
        }
      });

    this._on( this.input, {
      autocompleteselect: function( event, ui ) {
        ui.item.option.selected = true;
        this._trigger( "select", event, {
          item: ui.item.option
        });
      },

      autocompletechange: "_removeIfInvalid"
    });
  },

  _createShowAllButton: function() {
    var input = this.input,
      wasOpen = false;

    $( "<a>" )
      .attr( "tabIndex", 1 )
      .attr( "title", "Show All Items" )
      .tooltip()
      .appendTo( this.wrapper )
      .button({
        icons: {
          primary: "ui-icon-triangle-1-s"
        },
        text: false
      })
      .removeClass( "ui-corner-all" )
      .addClass( "custom-combobox-toggle ui-corner-right" )
      .on( "mousedown", function() {
        wasOpen = input.autocomplete( "widget" ).is( ":visible" );
      })
      .on( "click", function() {
        input.trigger( "focus" );

        // Close if already visible
        if ( wasOpen ) {
          return;
        }

        // Pass empty string as value to search for, displaying all results
        input.autocomplete( "search", "" );
      });
  },

  _source: function( request, response ) {
    var matcher = new RegExp( $.ui.autocomplete.escapeRegex(request.term), "i" );
    response( this.element.children( "option" ).map(function() {
      var text = $( this ).text();
      if ( this.value && ( !request.term || matcher.test(text) ) )
        return {
          label: text,
          value: text,
          option: this
        };
    }) );
  },

    _removeIfInvalid: function( event, ui ) {

    // Selected an item, nothing to do
    if ( ui.item ) {
      return;
    }

    // Search for a match (case-insensitive)
    var value = this.input.val(),
      valueLowerCase = value.toLowerCase(),
      valid = false;
    this.element.children( "option" ).each(function() {
      if ( $( this ).text().toLowerCase() === valueLowerCase ) {
        this.selected = valid = true;
        return false;
      }
    });

    // Found a match, nothing to do
    if ( valid ) {
      return;
    }

    // Remove invalid value
    this.input
        .val( "" )
        .attr( "title", value + " didn't match any item" )
        .tooltip( "open" );
        this.element.val( "" );
        this._delay(function() {
            this.input.tooltip( "close" ).attr( "title", "" );
        }, 2500 );
        this.input.autocomplete( "instance" ).term = "";
    },

    _destroy: function() {
        this.wrapper.remove();
        this.element.show();
       }
    });

    $( "#combobox" ).combobox();
} );

function urlToClipboard() {
  /* Get the text field */
  var copyText = document.URL;
  /* Select the text field */
  copyText.select();
  /* Copy the text inside the text field */
  document.execCommand("Copy");
  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}
