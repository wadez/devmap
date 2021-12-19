<!--
@title Tips to Enhance TailwindCSS Projects
@tags HTML, CSS
@slug enhance-tailwindcss-projects
@description Read to discover ways to improve the quality of your TailwindCSS code. Many utility class names are redundant. Are you using the correct classes?
-->

Recently, TailwindCSS released version 3.0 and the framework remains highly popular. Do you know all the little tricks for cleaner code?

![Example of tailwindcss project](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4j6381quzw1d95bztbw6.png)
 
---

# 1. Aspect Ratio
A clean UI requires all cards and images to be perfectly sized across all devices. There are too many screen sizes to use responsive scaling units like `em`, `rem`, `%`, or `vh/vw` making media distorted on some platforms.

Forcing a size for media is non-trivial with pixels but how do you force a responsive ratio? Perhaps, a profile banner is 1500x500 pixels but user uploaded content makes preserving user experiences challenging. The answer is aspect ratio containers.

demo: https://play.tailwindcss.com/hBXgOiGwv7

    <iframe class="w-full aspect-video ..." 
            src="https://www.youtube.com/ ...">
    </iframe>


Aspect ratios will force the content to grow to the width of the container while auto-scaling the height to match the ratio to `16:9`.  A node with a width of `1920` will have a height of `1080` while on mobile it will scale to `320x180`.

---

#2. Inset Positioning
The inset technique plays nicely with aspect ratio containers. Perhaps, a square element needs nested scrolling content. The quickest solution is to use absolute positioning on a child element with full width and full height. Regardless this will take a few class names to correctly position the child element. 



![tailwindcss inset class](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7hysv1n1nntnz3ysw2xk.png)
 
However, Tailwind developers know this technique is common. Now a single utility class will handle all the positioning. Insets will fill or partially fill the entire parent node.

demo: https://play.tailwindcss.com/4ZTlx80ryN

    <!-- Pin to top left corner -->
    <div class="relative aspect-square ...">
      <div class="absolute left-0 top-0 h-1/2 w-1/2 ...">01</div>
    </div>
    
    <!-- Span top edge -->
    <div class="relative aspect-square ...">
      <div class="absolute inset-x-0 top-0 h-1/2 ...">02</div>
    </div>
    
    <!-- Pin to top right corner -->
    <div class="relative aspect-square ...">
      <div class="absolute top-0 right-0 h-1/2 w-1/2 ...">03</div>
    </div>
    
    <!-- Span left edge -->
    <div class="relative aspect-square ...">
      <div class="absolute inset-y-0 left-0 w-1/2 ...">04</div>
    </div>
    
    <!-- Fill entire parent -->
    <div class="relative aspect-square ...">
      <div class="absolute inset-0 ...">05</div>
    </div>
    
    <!-- Span right edge -->
    <div class="relative aspect-square ...">
      <div class="absolute inset-y-0 right-0 w-1/2 ...">06</div>
    </div>
    
    <!-- Pin to bottom left corner -->
    <div class="relative aspect-square ...">
      <div class="absolute bottom-0 left-0 h-1/2 w-1/2 ...">07</div>
    </div>
    
    <!-- Span bottom edge -->
    <div class="relative aspect-square ...">
      <div class="absolute inset-x-0 bottom-0 h-1/2 ...">08</div>
    </div>
    
    <!-- Pin to bottom right corner -->
    <div class="relative aspect-square ...">
      <div class="absolute bottom-0 right-0 h-1/2 w-1/2 ...">09</div>
    </div>


---

# Divided List Styling
Tailwind is not perfect and often requires custom CSS to match the list styles of other popular frameworks like Boostrap. The iconic design places borders between each list item. 

The style is preferable because it shows a clear distinction between list items without needing complex structures like table, flexbox, or grid. Moreover, lists are more compatible across browsers.

How do you quickly style a list like Bootstrap in Tailwind without writing custom CSS? Simple, use the `divide` utility. 

demo: https://play.tailwindcss.com/YpbjZdaJoU

    <ul class="divide-y border">
      <li class="p-3">a</li>
      <li class="p-3">b</li>
      <li class="p-3">c</li>
      <li class="p-3">d</li>
    </ul>

---
# Conclusion
Thank you for reading my post. Now you know a few ways to reduce the number of utility classes included in your code. Here is a final product that uses all the techniques mentioned above: https://play.tailwindcss.com/6mpXYGwfdE
