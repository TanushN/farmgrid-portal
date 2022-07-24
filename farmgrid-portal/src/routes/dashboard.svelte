<script>
  import {
    Header,
    HeaderUtilities,
    HeaderAction,
    HeaderGlobalAction,
    HeaderPanelLinks,
    HeaderPanelDivider,
    HeaderPanelLink,
    SideNav,
    SideNavItems,
    SideNavMenu,
    SideNavMenuItem,
    SideNavLink,
    SkipToContent,
    Content,
    Grid,
    Row,
    Column,
  } from "carbon-components-svelte";
  import SettingsAdjust from "carbon-icons-svelte/lib/SettingsAdjust.svelte";
  import UserAvatarFilledAlt from "carbon-icons-svelte/lib/UserAvatarFilledAlt.svelte";
  import SensorAnalytics from "./sensorAnalytics.svelte";

  import sensorAnalytics from "./sensorAnalytics.svelte";

  import {user} from "../stores";
  import { navigate } from "svelte-navigator";

  let isOpen1 = false;

  async function logout() {
    localStorage.removeItem("user");
    user.set(null);

    navigate("/", { replace: true });

  }

</script>

<Header company="FarmGrid" platformName="Portal">
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
  <HeaderUtilities>
    <HeaderAction
      bind:isOpen={isOpen1}
      icon={UserAvatarFilledAlt}
      closeIcon={UserAvatarFilledAlt}
    >
      <HeaderPanelLinks>
        <HeaderPanelDivider>Profile</HeaderPanelDivider>
        <HeaderPanelLink on:click={logout}>Logout</HeaderPanelLink>
      </HeaderPanelLinks>
    </HeaderAction>
  </HeaderUtilities>
</Header>

<Content>
  <SensorAnalytics />
</Content>
