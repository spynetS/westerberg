document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.getElementById("navbar");
  const nav = document.getElementById("nav");
  const list = document.getElementById("list");
  const showerButton = document.getElementById("shower");
  const toppx = 200 + navbar.offsetHeight;

  let currentActiveSection = null;
  let currentActiveParent = null;
  let currentActiveSublist = null;

  const updateNavPosition = () => {
    const scrollPosition = window.scrollY || window.pageYOffset;
    if (scrollPosition < toppx) {
      nav.style.top = toppx - scrollPosition + "px";
    } else {
      nav.style.top = "0px";
    }
  };

  const isInView = (element) => {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.top <=
        (window.innerHeight || document.documentElement.clientHeight) / 10
    );
  };

  const logSectionInView = () => {
    let mostViewedSection = null;
    const sections = document.querySelectorAll("section");
    sections.forEach((section) => {
      if (isInView(section)) {
        mostViewedSection = section;
      }
    });
    return mostViewedSection;
  };

  const highlightNav = () => {
    const mostViewed = logSectionInView();
    if (mostViewed && mostViewed !== currentActiveSection) {
      // Update active section and corresponding nav item
      currentActiveSection = mostViewed;
      const matchedATag = document.querySelector(
        `a[href*="#${mostViewed.id}"]`,
      );
      if (matchedATag) {
        // Remove active class from previous nav item
        if (currentActiveParent) {
          currentActiveParent.classList.remove("btn", "btn-primary");
        }
        // Add active class to current nav item
        matchedATag.classList.add("btn", "btn-primary");

        // Show sublist for current section and hide previous sublist
        const newSublist = matchedATag.nextElementSibling;
        if (newSublist && newSublist.tagName === "UL") {
          newSublist.style.display = "block";
          if (currentActiveSublist && currentActiveSublist !== newSublist) {
            currentActiveSublist.style.display = "none";
          }
          currentActiveSublist = newSublist;
        }

        // Update current active parent
        currentActiveParent = matchedATag;
      }
    }
  };

  const fixHeight = () => {
    updateNavPosition();
    highlightNav();
  };

  const populateNavList = () => {
    const sections = document.querySelectorAll("section");
    sections.forEach((section) => {
      const h2 = section.querySelector("h2");
      if (h2) {
        const li = document.createElement("li");
        const anchor = document.createElement("a");
        anchor.setAttribute("href", `#${section.id}`);
        anchor.setAttribute("name", "nava");
        anchor.textContent = h2.textContent;
        li.appendChild(anchor);
        list.appendChild(li);

        const h3s = section.querySelectorAll("h3");
        if (h3s.length > 0) {
          const sublist = document.createElement("ul");
          sublist.style.display = "none"; // Hide sublist initially
          h3s.forEach((h3) => {
            const subli = document.createElement("li");
            const subanchor = document.createElement("a");
            subanchor.setAttribute("href", `#${section.id}`);
            subanchor.setAttribute("name", "nava");
            subanchor.textContent = h3.textContent;
            subli.appendChild(subanchor);
            sublist.appendChild(subli);
          });
          li.appendChild(sublist); // Append sublist to the parent li
        }
      }
    });
  };

  const showNav = () => {
    list.classList.remove("hidden");
    list.classList.add("pt-12");
    showerButton.textContent = "<";
    showerButton.onclick = hideNav;
  };

  const hideNav = () => {
    list.classList.add("hidden");
    list.classList.remove("pt-12");
    showerButton.textContent = ">";
    showerButton.onclick = showNav;
  };

  window.addEventListener("scroll", fixHeight);
  showerButton.onclick = showNav;

  populateNavList();
  updateNavPosition();
});
