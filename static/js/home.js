document.getElementById("homeVideo").addEventListener("loadedmetadata", start);
let video_length = 0;
let fadeout = 39000;
let i = 0;
let removeTimeoutId;
let addTimeoutId;

let quotes = [
  [
    "Vi ser mycket långsiktigt på vårt företagande och vår målsättning är att även detta skall speglas i långvariga och trevliga kontakter med våra hyresgäster.",
    8000,
  ],
  ["Vi har fastigheter i, Söderköping, Norrköping, Åby", 8000],
];

function changeText() {
  let para = document.getElementById("para");
  let inner = `<p class="animate-in fade-id slide-in-from-left-72 duration-700 lg:text-2xl md:text-lg font-semibold text-white w-[200px] md:w-[400px]">${quotes[i][0]}</p>`;
  para.innerHTML = inner;
  setTimeout(changeText, quotes[i][1]);
  i = (i + 1) % quotes.length;
}

function add() {
  let over = document.getElementById("overvideo");
  over.classList.remove("opacity-0");
  removeTimeoutId = setTimeout(remove, fadeout);
}

function remove() {
  let over = document.getElementById("overvideo");
  over.classList.add("opacity-0");
  addTimeoutId = setTimeout(add, video_length - fadeout);
}

function start() {
  var x = document.getElementById("homeVideo").duration;
  video_length = x * 1000;
  i = 0;
  removeTimeoutId = setTimeout(remove, fadeout);
  changeText();
}

document.addEventListener("visibilitychange", function () {
  if (document.visibilityState === "visible") {
    document.getElementById("homeVideo").currentTime = 0;
    clearTimeout(removeTimeoutId);
    clearTimeout(addTimeoutId);
    start();
  }
});
const callback = (entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
    } else {
      entry.target.classList.remove("is-visible");
    }
  });
};

// Create an IntersectionObserver instance with the callback
const observer = new IntersectionObserver(callback, {
  root: null, // Use the viewport as the root
  rootMargin: "0px",
  threshold: 0.1, // Trigger if at least 10% of the element is visible
});

// Get all the div elements to be observee
const divs = document.getElementsByClassName("news-card");

// Convert HTMLCollection to an array and then use forEach
Array.prototype.forEach.call(divs, (div) => {
  observer.observe(div);
});
