import os
import re
import shutil

# Paths
posts_dir         = "/home/arenmohanix/Documents/arenblog/content/posts/"
attachments_dir   = "/home/arenmohanix/Documents/obsidian-folder/private/"
static_images_dir = "/home/arenmohanix/Documents/arenblog/static/images/"

# Process each markdown file
for md in os.listdir(posts_dir):
    if not md.endswith(".md"):
        continue

    path = os.path.join(posts_dir, md)
    print(f"\n⏳ Processing {md}…")
    text = open(path).read()

    # Match both .png and .jpg (case-insensitive)
    pattern = re.compile(r'!\[\[([^]]+)\]\]', re.IGNORECASE)
    matches = pattern.findall(text)
    if not matches:
        print(" • No image embeds found.")
        continue

    for img in matches:
        # Try jpg first, then png if not found
        for ext in ["png", "jpg"]:
            src_name = img.rsplit('.', 1)[0] + "." + ext
            src = os.path.join(attachments_dir, src_name)
            if os.path.exists(src):
                tgt = os.path.join(static_images_dir, src_name)
                print(f" • Copying {src_name} → static/images/")
                shutil.copy(src, tgt)
                
                # Replace in Markdown to use correct extension
                text = text.replace(f"![[{img}]]", f"![Image](/images/{src_name})")
                break
        else:
            print(f" ⚠️  Image not found for embed: [[{img}]]")

    # Write back
    with open(path, "w") as f:
        f.write(text)

print("\n✅ Done.")
