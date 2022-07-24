
<script lang="ts">
  import { Router, Link, Route } from "svelte-navigator";
  import Dashboard from "./routes/dashboard.svelte";
  import Login from "./routes/login.svelte";
  import ProtectedRoute from "./routes/protectedRoute.svelte";
  import "carbon-components-svelte/css/all.css";
  import "@carbon/styles/css/styles.css";
  import { Button } from "carbon-components-svelte";
  import {theme} from "./stores";
  import Signup from "./routes/signup.svelte";

  $: document.documentElement.setAttribute("theme", $theme);
</script>

<main>
  <Router>
    <div>
      <Route path="/login" component={Login} />
      <ProtectedRoute path="/" component={Dashboard} />
      <ProtectedRoute path="/signup" component={Signup}/>
    </div>
  </Router>
</main>