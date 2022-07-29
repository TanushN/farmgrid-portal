<script>
  import { user } from "../stores";
  import { navigate } from "svelte-navigator";
  import {
    TextInput,
    PasswordInput,
    Button,
    ToastNotification,
  } from "carbon-components-svelte";

  import Api from "../util/api";

  async function login() {
    try {
      const response = await Api.post("/auth/login", {
        email: email,
        password: password,
      });

      localStorage.setItem("user", response.email);

      user.set(response.email);

      navigate("/", { replace: true });
    } catch (error) {
      console.error(error.response.data.detail);
      toastError = error.response.data.detail;
      showErrorToast = true;
    }
  }

  let email;
  let password;

  let showErrorToast = false;
  let toastError = "";
</script>

<main>
  <div class="login">
    <h3>Login</h3>
    <TextInput
      bind:value={email}
      labelText="Email"
      placeholder="example@gmail.com"
    />
    <PasswordInput
      bind:value={password}
      labelText="Password"
      placeholder="Enter password..."
    />
    <div width="fit-content">
      <Button on:click={login}>Login</Button>
    </div>
    <a href="signup">Don't have an account? Sign up here instead.</a>
  </div>
  {#if showErrorToast}
    <ToastNotification
      lowContrast
      kind="error"
      title="Error"
      subtitle={toastError}
      caption={new Date().toLocaleString()}
      on:close={() => showErrorToast=false}
    />
  {/if}
</main>

<style>
  .login {
    display: flex;
    position: absolute;
    row-gap: 1rem;
    flex-direction: column;
    width: 20%;
    justify-content: flex-start;
    top: 40%;
    left: 40%;
    right: 40%;
  }
</style>
