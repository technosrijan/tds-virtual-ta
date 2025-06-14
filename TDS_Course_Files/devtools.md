## Browser: DevTools

Chrome DevTools is the de facto standard for web development and data analysis in the browser.
You'll use this a lot when debugging and inspecting web pages.

Here are the key features you'll use most:

1. **Elements Panel**

   - Inspect and modify HTML/CSS in real-time
   - Copy CSS selectors for web scraping
   - Debug layout issues with the Box Model

   ```javascript
   // Copy selector in Console
   copy($0); // Copies selector of selected element
   ```

2. **Console Panel**

   - JavaScript REPL environment
   - Log and debug data
   - Common console methods:

   ```javascript
   console.table(data); // Display data in table format
   console.group("Name"); // Group related logs
   console.time("Label"); // Measure execution time
   ```

3. **Network Panel**
   - Monitor API requests and responses
   - Simulate slow connections
   - Right-click on a request and select "Copy as fetch" to get the request.
4. **Essential Keyboard Shortcuts**
   - `Ctrl+Shift+I` (Windows) / `Cmd+Opt+I` (Mac): Open DevTools
   - `Ctrl+Shift+C`: Select element to inspect
   - `Ctrl+L`: Clear console
   - `$0`: Reference currently selected element
   - `$$('selector')`: Query selector all (returns array)

Videos from Chrome Developers (37 min total):

- Fun & powerful: Intro to Chrome DevTools (5 min)
- Different ways to open Chrome DevTools (5 min)
- Faster DevTools navigation with shortcuts and settings (3 min)
- How to log messages in the Console (6 min)
- How to speed up your workflow with Console shortcuts (6 min)
- HTML vs DOM? Let’s debug them (5 min)
- Caching demystified: Inspect, clear, and disable caches (7 min)
- Console message logging (6 min)
- Console workflow shortcuts (6 min)
- HTML vs DOM debugging (5 min)
- Cache inspection and management (7 min)