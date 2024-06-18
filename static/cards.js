function cards() {
  const callback = (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
      } else {
        entry.target.classList.remove("is-visible");
      }
      console.log("asdasd");
    });
  };

  // Create an IntersectionObserver instance with the callback
  const observer = new IntersectionObserver(callback, {
    root: null, // Use the viewport as the root
    rootMargin: "0px",
    threshold: 0.1, // Trigger if at least 10% of the element is visible
  });

  // Get all the div elements to be observed
  const divs = document.querySelectorAll("div");

  // Start observing each div
  divs.forEach((div) => {
    observer.observe(div);
  });
}
