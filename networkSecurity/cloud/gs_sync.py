import os

class gssync:
    def sync_to_gcp(self, folder, gcp_bucket_url):
        command=f"gsutil rsync -r {folder} {gcp_bucket_url}"
        os.system(command)

    def sync_from_gcp(self, folder, gcp_bucket_url):
        command=f"gsutil rsync -r {gcp_bucket_url} {folder} "
        os.system(command)