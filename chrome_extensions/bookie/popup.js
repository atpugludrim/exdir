$('#search').change(function(){
    $('#bookmarks').empty();
    dumpBookmarks($('#search').val());
});
function dumpBookmarks(query){
var bmt = chrome.bookmarks.getTree(function(bmt){
    $('#bookmarks').append(dumpTreeNodes(bmt,query));
});
}
function dumpTreeNodes(bmt,query){
    var list=$('<ul>');
    for ( var i = 0; i < bmt.length; i++){
        list.append(dumpNode(bmt[i],query));
    }
    return list;
}

function dumpNode(node,query){
    if(node.title){
        if(query && !node.children){
            if(String(node.title.toLowerCase()).indexOf(query.toLowerCase())==-1){
                return $('<span></span>');
            }
        }
        var anchor = $('<a>');
        anchor.attr('href',node.url);
        anchor.text(node.title);
        var span=$('<span>');
        span.hover(function(){console.log('h');}).append(anchor);
    }
        var li=$(node.title ? '<li>':'<div>').append(span);
        if(node.children && node.children.length > 0){
            li.append(dumpTreeNodes(node.children,query));
        }
    return li;
}
// document.addEventListener('DOMContentLoaded', function () {
//   dumpBookmarks();
// });
