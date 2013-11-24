$(function() {
    var availableBeers = [
        "Yuengling",
        "Anchor Steam",
        "Lukewarm Keystone light"
    ];
    $( "#beer" ).autocomplete({
        source: availableBeers
    });
});
