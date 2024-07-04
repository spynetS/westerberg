/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../buildings/templates/**/*.html",
    "../news/templates/**/*.html",
    "../rentals/templates/**/*.html",
    "../servicereport/templates/**/*.html",
    "../intrestreport/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui"), require("tailwindcss-animate")],
  daisyui: {
    themes: [
      "light",
      "dark",
      "corporate",
      "nord",
      "fantasy",
      {
        mytheme: {
          primary: "#2a2d5f",

          secondary: "#006e56",

          accent: "#474555",

          neutral: "#aba9bb",

          "base-100": "#ffffff",

          info: "#003d29",

          success: "#006e56",

          warning: "#e8d5b5",

          error: "#5d1b1e",
        },
      },
    ],
  },
};
