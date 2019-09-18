document.write('<style>.acifc {-webkit-overflow-scrolling: touch; overflow-x: auto;} .acifc iframe {width:100%;}</style>');
document.write('<div id="ac-LYauM4DZEYzSQJMfFoL3-696" class="acifc"><iframe data-description="javascript-embed" id="ac-iframe-LYauM4DZEYzSQJMfFoL3-696" name="ac-iframe-LYauM4DZEYzSQJMfFoL3-696" src="https://www.availabilitycalendar.com//embed/LYauM4DZEYzSQJMfFoL3/en-0-0-1-1-0-0-0-0-0-0-0-1-0/?iframe=true" height="1000px" width="100%" frameborder="0" allowtransparency="true"></iframe></div>');

window.addEventListener('message', function(e) {
	var data = e.data.split('___'), bodyHeight = parseInt(data[0]), iframe_id = data[1];
	
	//current height of the iframe
	var iframeheight = parseInt(document.getElementById('ac-iframe-LYauM4DZEYzSQJMfFoL3-696').scrollHeight);
	
	if(iframe_id == 'ac-iframe-LYauM4DZEYzSQJMfFoL3-696' && (bodyHeight - iframeheight > 5 || iframeheight - bodyHeight > 5)) //those 5px is because of Edge, the page whould grow 4px at every update somehow.
		document.getElementById('ac-iframe-LYauM4DZEYzSQJMfFoL3-696').style.height = (bodyHeight) + '0px'; 
		
	if(self != top && document.body.children.length == 1 && document.body.children[0].id == "ac-LYauM4DZEYzSQJMfFoL3-696") //only when this script is embedded in another iframe, like with Wix sites.
		document.body.style.margin = "0px";
		
} , false);
