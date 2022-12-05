import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { Server } from "http";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    proxy: {
      "/api": { target: "http://127.0.0.1:8000/" },
      "/admin": { target: "http://127.0.0.1:8000/" },
      "/static": { target: "http://127.0.0.1:8000/" },
      //"/api/home": "http://127.0.0.1:8000/",
      //"/api/accounts": "http://127.0.0.1:8000/",
    },
  },
});
