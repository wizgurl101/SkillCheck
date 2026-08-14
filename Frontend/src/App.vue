<script setup lang="ts">
import { ref } from "vue";

const jobPosting = ref("");
const resume = ref<File | null>(null);
const showMissingSkills = ref(false);
</script>

<template>
  <v-app>
    <v-main>
      <v-container class="fill-height d-flex align-center justify-center">
        <div class="w-100" style="max-width: 600px">
          <!-- Skill Check Form -->
          <v-card class="pa-8">
            <v-card-title class="text-h4 text-center mb-6">
              Skill Check
            </v-card-title>

            <v-card-text>
              <v-textarea
                v-model="jobPosting"
                label="Post Job Posting"
                placeholder="Paste the job posting here..."
                variant="outlined"
                rows="8"
                class="mb-4"
              />

              <v-file-input
                v-model="resume"
                label="Upload Resume"
                accept=".pdf"
                variant="outlined"
                show-size
              />

              <v-btn
                color="primary"
                size="large"
                block
                class="mt-6"
                @click="showMissingSkills = true"
              >
                Check Skills
              </v-btn>
            </v-card-text>
          </v-card>

          <!-- Missing Skills -->
          <v-card v-if="showMissingSkills" class="pa-6 mt-6">
            <v-card-title class="text-h5"> Missing Skills </v-card-title>

            <v-card-text>
              <!-- Missing skills will eventually appear here -->
            </v-card-text>
          </v-card>
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>
