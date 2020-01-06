import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  @import url("https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap");

  * {
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
  }

  html,
  body,
  #root {
    min-width: 100%;
  }

  body {
    background-color: #fafafa;
    -webkit-font-smoothing: antialiased !important;
  }

  body,
  input,
  button {
    font-family: "Roboto", Arial, Helvetica, sans-serif;
    font-size: 14px;
  }
`;

export default GlobalStyle;
