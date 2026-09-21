# GitHub access before publication

Checked on 21 September 2026 using the authenticated GitHub API:

- Existing demo repositories belong to `Infra-as-code-ICA0024-TalTech`.
- The organization has **Read** base repository permission.
- Existing demo repositories are private.

Under this setting, every organization member inherits read access to new private repositories. A repository-specific permission cannot reduce inherited access. Therefore simply creating `Infra-as-code-ICA0024-TalTech/questionnaires` as private would expose its answers to all organization members.

To restrict it to selected instructors in that organization, an owner would need to change the organization base permission to **None**, preserve students' access to demo repositories through explicit team/repository grants, and grant access to the questionnaire repository only to the intended instructors. Organization owners retain access. Review existing grants before changing the base permission because this is an organization-wide change.

A private repository owned by the instructor's personal account is an alternative that avoids changing access to the teaching organization. Organization membership alone would not grant access to a personally owned private repository.

The local repository is ready. No GitHub repository has been created or pushed, and no organization permissions have been changed. Hosting is pending the instructor's choice.

References:

- [Setting base permissions for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization)
- [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
