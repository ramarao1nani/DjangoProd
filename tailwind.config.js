/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'media',
  content: [
    './myapp/templates/myapp/*.html',
    './users/templates/users/*.html',
    './users/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
