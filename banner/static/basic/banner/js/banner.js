if (typeof $ != 'undefined')
{

$(document).ready(function(){

    // Load DFP ads when listing refreshes
    $(document).bind('onListingRefresh', function(event, target){
        $('div.gpt-ad', target).each(function(){                    
            var el = $(this);
            var id = el.attr('id');
            var slot_name = el.attr('slot_name');
            var width = parseInt(el.attr('width'));
            var height = parseInt(el.attr('height'));
            var targeting_key = el.attr('targeting_key');
            var targeting_values = el.attr('targeting_values').split('|');
            googletag.defineSlot(slot_name, [width, height], id).addService(googletag.pubads()).setTargeting(targeting_key, targeting_values);
            // Someday DFP may provide disableSingleRequest. Then it must be used here.
            googletag.enableServices();
            googletag.display(id); 
        });
    });

});

}
