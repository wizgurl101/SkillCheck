import { createApp } from "vue";
import App from "./App.vue";

import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,

  theme: {
    defaultTheme: "skillCheckTheme",

    themes: {
      skillCheckTheme: {
        colors: {
          background: "#1D546D",
          surface: "#F3F4F4",
          primary: "#061E29",
          "on-background": "#061E29",
          "on-surface": "#061E29",
        },
      },
    },
  },
});

createApp(App).use(vuetify).mount("#app");
