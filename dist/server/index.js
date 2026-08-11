export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const routeAliases = {
      "/assignment-2/": "/assignment-2.html",
      "/homework/": "/homework.html",
      "/lab3/": "/lab3.html",
      "/organizers/": "/organizers.html",
      "/sponsor": "/sponsor-deck.html",
      "/sponsor/": "/sponsor-deck.html"
    };

    if (routeAliases[url.pathname]) {
      return Response.redirect(new URL(routeAliases[url.pathname], url), 302);
    }

    const directResponse = await env.ASSETS.fetch(request);
    if (directResponse.status !== 404) return directResponse;

    const assetUrl = new URL(request.url);
    assetUrl.pathname = url.pathname.endsWith("/")
      ? `${url.pathname}index.html`
      : `${url.pathname}/index.html`;

    const indexResponse = await env.ASSETS.fetch(new Request(assetUrl, request));
    if (indexResponse.status !== 404 || url.pathname !== "/") return indexResponse;

    assetUrl.pathname = "/index.html";
    return env.ASSETS.fetch(new Request(assetUrl, request));
  },
};
