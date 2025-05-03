---
title: Cyber Log
date: 2024-11-06
draft: false
tags:
  - arenredd
  - tag2
---
!![Image Description](/images/backiee-298776-landscape.png)

Today, I am attempting to create my own cryptocurrency using Kali Linux. It has been quite challenging, but I successfully created a cryptocurrency with the Solana wallet. However, I am having trouble customizing it.

I also came across a YouTube video about running Windows on Linux and vice versa using WSL, which seemed interesting. I've started the process of setting up a dual boot. My first step was to split my disk partition, but I encountered a problem: since Kali Linux is installed on the main partition, I can’t split it directly from my installed Kali system.

To work around this, I installed Kali Linux for live boot on a USB drive. After splitting my partition, I flashed the USB drive with the Windows 11 ISO. However, when I installed Windows, it did not recognize my UN-allocated partition. To resolve this, I found a compatible storage driver for my laptop and saved it on the same USB drive with the Windows ISO.

After finishing the Windows installation, which took about half a day, I restarted my laptop only to boot directly into Windows without any menu options to select Kali Linux. Later in the evening, I repaired the GRUB boot-loader for both Kali Linux and Windows using the Kali live boot. I discovered that I couldn't resize, move, or safely reinstall GRUB directly from my installed system, which is why the live boot was necessary.

After repairing the GRUB menu, I watched more YouTube videos about quantum computers. That’s how my day ended. I realized I actually enjoy fixing OS-level problems.
