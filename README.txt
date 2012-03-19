IISMonitor
----------

IISMonitor collects key metrics from Microsoft IIS. The metrics are collected
using Windows Perfmon and require no agent to be installed on the IIS server.

The following metrics will be collected and graphed for Microsoft IIS.

    * Connections Attempts
    * Throughput (Bytes & Files)
    * Requests (GET, HEAD, POST, CGI, ISAPI)
        Standard: GET, HEAD, POST, CGI, ISAPI
        WebDAV: PUT, COPY, MOVE, DELETE, OPTIONS, PROPFIND, PROPPATCH, MKCOL
        Other: SEARCH, TRACE, LOCK, UNLOCK


Follow these steps to setup your IIS server to have this information collected.

    1. Verify that your Zenoss Windows service account has access to the IIS
       server. Within Zenoss this is specified using zWinUser and zWinPassword.

    2. Bind the IIS performance template to the IIS server device within Zenoss.
