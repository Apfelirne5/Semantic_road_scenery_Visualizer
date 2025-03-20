function handleBehaviourDirectionRadioButton(radioButton) {
  let c = document.getElementById('bssd_world').classList;

  c.remove('showBehaviourDirection_forward');
  c.remove('showBehaviourDirection_backward');

  let direction = radioButton.value;

  if (direction === 'forward' || direction === 'backward') {
    c.add('showBehaviourDirection_' + direction)
  }
    //alert(c);
}

function handleTrafficLightActiveRadioButton(radioButton) {
  let c2 = document.getElementById('bssd_world').classList;

  c2.remove('showTla_Yes');
  c2.remove('showTla_No');

  let status = radioButton.value;

  if (status === 'Yes' || status === 'No') {
    c2.add('showTla_' + status)
  }
    //alert(c);
}


function getId(id) {
  const el = document.getElementById(id);
  if (!el) throw Error(`cannot find #${id}`);
  return el;
}

function getOffset(el) {
  let rect = el.getBoundingClientRect();
  return {
    left: rect.left + window.pageXOffset,
    top: rect.top + window.pageYOffset,
    width: rect.width || el.offsetWidth,
    height: rect.height || el.offsetHeight
  };
}

function connect(div2, div1, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // bottom right
  let x1 = off1.left + off1.width;
  let y1 = off1.top + (off1.height) / 2;
  // top right
  let x2 = off2.left;
  let y2 = off2.top + (off2.height) / 2;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div style='padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}

function connectLastSegment(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center left
  let x1 = off1.left ;
  let y1 = off1.top + (off1.height) / 2;
  // center right
  let x2 = off2.left + off2.width;
  let y2 = off2.top + (off2.height) / 2;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}


function connectNextSegment(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center left
  let x1 = off1.left + (off1.width);
  let y1 = off1.top + (off1.height) / 2;
  // center right
  let x2 = off2.left;
  let y2 = off2.top + (off2.height) / 2 ;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}


function connectSegmentTop(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center top
  let x1 = off1.left + (off1.width);
  let y1 = off1.top ;
  // up 3x
  let x2 = off1.left + (off1.width);
  let y2 = off2.top;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}

function connectSegmentBottom(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center bottom
  let x1 = off1.left + (off1.width);
  let y1 = off1.top + (off1.height);
  // down 3x
  let x2 = off1.left + (off1.width);
  let y2 = off2.top + (off2.height);
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}

function connectLaneTop(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center top
  let x1 = off1.left;
  let y1 = off1.top ;
  // center bottom
  let x2 = off1.left;
  let y2 = off2.top + off2.height;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}

function connectLaneBottom(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center bottom
  let x1 = off1.left;
  let y1 = off1.top + off1.height;
  // center top
  let x2 = off1.left;
  let y2 = off2.top;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}

function connectWayFirst(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center bottom
  let x1 = off1.left ;
  let y1 = off1.top + (off1.height) / 2;
  // center right
  let x2 = -off2.left;
  let y2 = off1.top + (off1.height) / 2;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}

function connectWayLast(div1, div2, color, thickness) { // draw a line connecting elements
  let off1 = getOffset(div1);
  let off2 = getOffset(div2);
  // center bottom
  let x1 = off1.left + (off1.width);
  let y1 = off1.top + (off1.height) / 2;
  // center right
  let x2 = off2.left + 400;
  let y2 = off1.top + (off1.height) / 2;
  // distance
  let length = Math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
  // center
  let cx = ((x1 + x2) / 2) - (length / 2);
  let cy = ((y1 + y2) / 2) - (thickness / 2);
  // angle
  let angle = Math.atan2((y1 - y2), (x1 - x2)) * (180 / Math.PI);
  // make hr
  let htmlLine = "<div class='showonhover' style='background: url(../templates/signs/arrow.svg); background-size: contain; background-repeat: repeat-x; border: 2px solid transparent; border-radius: 1em; padding:0px; margin:0px; height:" + thickness + "px; background-color:" + color + "; line-height:1px; position:absolute; left:" + cx + "px; top:" + cy + "px; width:" + length + "px; -moz-transform:rotate(" + angle + "deg); -webkit-transform:rotate(" + angle + "deg); -o-transform:rotate(" + angle + "deg); -ms-transform:rotate(" + angle + "deg); transform:rotate(" + angle + "deg);' />";
  //
  // alert(htmlLine);
  document.querySelector('.lines').innerHTML += htmlLine;
}


function deleteElement() {
    var x, i;
  x = document.querySelectorAll(".showonhover");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
}



/*
const speedDiv = document.querySelector("div.bssd_speed_max"),
  Container = document.querySelector(".speedy_container");

Container.addEventListener("mouseover", e => {
  if(e.target.matches(".speedy_container > *")) speedDiv.textContent = e.target.dataset.speed;
})

Container.addEventListener("mouseout", e => {
  if(e.target.matches(".speedy_container > *")) speedDiv.textContent = speedDiv.dataset.speed;
})
*/