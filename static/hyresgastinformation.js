document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.getElementById("navbar");
  const nav = document.getElementById("nav");
  const list = document.getElementById("list");
  const showerButton = document.getElementById("shower");
  const toppx = 200 + navbar.offsetHeight;

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
    if (mostViewed) {
      const aTags = document.getElementsByName("nava");
      aTags.forEach((tag) => (tag.className = ""));
      const matchedATag = document.querySelector(
        `a[href*="#${mostViewed.id}"]`,
      );
      if (matchedATag) {
        matchedATag.className = "btn btn-primary";
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
      }

      const h3s = section.querySelectorAll("h3");
      if (h3s.length > 0) {
        const sublist = document.createElement("ul");
        h3s.forEach((h3) => {
          const subli = document.createElement("li");
          const subanchor = document.createElement("a");
          subanchor.setAttribute("href", `#${section.id}`);
          subanchor.setAttribute("name", "nava");
          subanchor.textContent = h3.textContent;
          subli.appendChild(subanchor);
          sublist.appendChild(subli);
        });
        const sublistItem = document.createElement("li");
        sublistItem.appendChild(sublist);
        list.appendChild(sublistItem);
      }
    });
  };

  const showNav = () => {
    nav.classList.remove("-left-[400px]");
    list.classList.add("pt-12");
    showerButton.textContent = "<";
    showerButton.onclick = hideNav;
  };

  const hideNav = () => {
    nav.classList.add("-left-[400px]");
    list.classList.remove("pt-12");
    showerButton.textContent = ">";
    showerButton.onclick = showNav;
  };

  window.addEventListener("scroll", fixHeight);
  showerButton.onclick = showNav;

  populateNavList();
  updateNavPosition();
});
