import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  // ... your config ...
  plugins: [svelte() /* ... your plugins ... */],
  // Add this line:
  optimizeDeps: { include: ["@carbon/charts"], exclude: ["svelte-navigator"] },
});
