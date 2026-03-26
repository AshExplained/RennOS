#!/usr/bin/env node
/**
 * RennOS Update Script
 * Pulls latest system files from GitHub without touching your personal data.
 *
 * Usage: node update.js
 */

const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const REPO_URL = "https://github.com/AshExplained/RennOS.git";
const REMOTE_NAME = "rennos-upstream";

// Colors (ANSI)
const c = {
  red: (s) => `\x1b[31m${s}\x1b[0m`,
  green: (s) => `\x1b[32m${s}\x1b[0m`,
  yellow: (s) => `\x1b[33m${s}\x1b[0m`,
  cyan: (s) => `\x1b[36m${s}\x1b[0m`,
};

const info = (msg) => console.log(`${c.cyan("[INFO]")} ${msg}`);
const ok = (msg) => console.log(`${c.green("[OK]")} ${msg}`);
const warn = (msg) => console.log(`${c.yellow("[WARN]")} ${msg}`);
const error = (msg) => console.log(`${c.red("[ERROR]")} ${msg}`);

function run(cmd) {
  return execSync(cmd, { encoding: "utf-8", stdio: "pipe" }).trim();
}

function runSafe(cmd) {
  try {
    return run(cmd);
  } catch {
    return null;
  }
}

// ---------------------------------------------------------------------------
// Protected files — NEVER overwrite (personal data)
// ---------------------------------------------------------------------------
const PROTECTED = new Set([
  ".claude/ceo-memory/user_profile.md",
  ".claude/ceo-memory/active_projects.md",
  ".claude/ceo-memory/decisions.md",
  ".claude/ceo-memory/feedback.md",
  ".claude/ceo-memory/MEMORY.md",
  ".claude/settings.local.json",
  "data/brand/brand-dna.md",
  "data/strategy/audience-personas.md",
  "data/strategy/competitive-landscape.md",
  "data/strategy/quarterly-roadmap.md",
  "update.js",
]);

function isProtected(file) {
  return PROTECTED.has(file);
}

function isAgentMemory(file) {
  return /^\.claude\/agent-memory\/[^/]+\/MEMORY\.md$/.test(file);
}

function isDataFile(file) {
  return file.startsWith("data/") && !file.endsWith("/.gitkeep") && !file.endsWith(".gitkeep");
}

function isVaultFile(file) {
  return file.startsWith("vault/") && !file.endsWith("/.gitkeep") && !file.endsWith(".gitkeep");
}

function isGitkeep(file) {
  return file.endsWith(".gitkeep");
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

console.log("");
console.log("==========================================");
console.log("  RennOS Updater");
console.log("==========================================");
console.log("");

// Check we're in a git repo
if (!runSafe("git rev-parse --is-inside-work-tree")) {
  error("Not inside a git repository. Run this from your RennOS root.");
  process.exit(1);
}

// Add upstream remote if not present
if (!runSafe(`git remote get-url ${REMOTE_NAME}`)) {
  info(`Adding upstream remote: ${REPO_URL}`);
  run(`git remote add ${REMOTE_NAME} ${REPO_URL}`);
}

// Fetch latest
info("Fetching latest from RennOS upstream...");
try {
  run(`git fetch ${REMOTE_NAME} main --quiet`);
} catch {
  error(`Failed to fetch from ${REPO_URL}`);
  error("Check your internet connection and try again.");
  process.exit(1);
}
ok("Fetched latest version");

// Get list of upstream files
const upstreamFiles = run(`git ls-tree -r --name-only ${REMOTE_NAME}/main`).split("\n").filter(Boolean);

const updated = [];
const created = [];
const skipped = [];
const newAgents = [];

console.log("");
info("Comparing with upstream...");

for (const file of upstreamFiles) {
  // PROTECTED — never overwrite
  if (isProtected(file)) {
    skipped.push(`${file} (protected)`);
    continue;
  }

  // AGENT MEMORY — only create new, never overwrite existing
  if (isAgentMemory(file)) {
    if (!fs.existsSync(file)) {
      const dir = path.dirname(file);
      fs.mkdirSync(dir, { recursive: true });
      const content = run(`git show ${REMOTE_NAME}/main:${file}`);
      fs.writeFileSync(file, content);
      newAgents.push(file);
    }
    continue;
  }

  // DATA FILES — only create new, never overwrite existing content
  if (isDataFile(file)) {
    if (!fs.existsSync(file)) {
      const dir = path.dirname(file);
      fs.mkdirSync(dir, { recursive: true });
      const content = run(`git show ${REMOTE_NAME}/main:${file}`);
      fs.writeFileSync(file, content);
      created.push(`${file} (new data placeholder)`);
    } else {
      skipped.push(`${file} (existing data)`);
    }
    continue;
  }

  // VAULT — only create .gitkeep for new dirs, never overwrite content
  if (isVaultFile(file)) {
    skipped.push(`${file} (vault)`);
    continue;
  }

  // GITKEEP — create new directory structures
  if (isGitkeep(file) && !fs.existsSync(file)) {
    const dir = path.dirname(file);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(file, "");
    created.push(`${file} (new directory)`);
    continue;
  }

  // SYSTEM FILES — always overwrite
  const dir = path.dirname(file);
  if (dir !== ".") {
    fs.mkdirSync(dir, { recursive: true });
  }

  if (fs.existsSync(file)) {
    // Check if actually changed
    const localHash = runSafe(`git hash-object "${file}"`);
    const upstreamHash = runSafe(`git rev-parse "${REMOTE_NAME}/main:${file}"`);

    if (localHash !== upstreamHash) {
      const content = run(`git show ${REMOTE_NAME}/main:${file}`);
      fs.writeFileSync(file, content);
      updated.push(file);
    }
  } else {
    const content = run(`git show ${REMOTE_NAME}/main:${file}`);
    fs.writeFileSync(file, content);
    created.push(file);
  }
}

// ---------------------------------------------------------------------------
// Summary
// ---------------------------------------------------------------------------

console.log("");
console.log("==========================================");
console.log("  Update Summary");
console.log("==========================================");
console.log("");

if (updated.length > 0) {
  ok(`Updated (${updated.length} files):`);
  for (const f of updated) {
    console.log(`    ${f}`);
  }
  console.log("");
}

if (created.length > 0) {
  ok(`Created (${created.length} files):`);
  for (const f of created) {
    console.log(`    ${f}`);
  }
  console.log("");
}

if (newAgents.length > 0) {
  ok(`New agents (${newAgents.length}):`);
  for (const f of newAgents) {
    const agent = path.basename(path.dirname(f));
    console.log(`    ${agent}`);
  }
  console.log("");
}

if (updated.length === 0 && created.length === 0 && newAgents.length === 0) {
  ok("Already up to date! No changes needed.");
}

console.log("");
info("Your personal data was not touched:");
info("  - user_profile.md, active_projects.md, decisions.md, feedback.md");
info("  - Agent memories (existing), data/ content, vault/ content");
console.log("");
console.log("==========================================");
console.log("  Done!");
console.log("==========================================");
console.log("");
