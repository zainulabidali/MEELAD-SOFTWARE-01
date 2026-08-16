export function generateGreenRoomHTML(f, programs, participantsMap, isCompact, formatLabel) {
    let htmlContent = '';
    const pageDivClass = isCompact ? 'program-card-compact' : 'program-page-standard';

    // Group programs by Category
    const groups = {};
    programs.forEach(p => {
        const catId = p.categoryId || 'unknown';
        if (!groups[catId]) {
            groups[catId] = {
                categoryName: p.categoryName || 'General',
                programs: []
            };
        }
        groups[catId].programs.push(p);
    });

    const sortedCatIds = Object.keys(groups).sort((a, b) => {
        return groups[a].categoryName.localeCompare(groups[b].categoryName);
    });

    sortedCatIds.forEach(catId => {
        const cat = groups[catId];
        const sortedPrograms = cat.programs.sort((a, b) => {
            return (a.programName || '').localeCompare(b.programName || '');
        });

        sortedPrograms.forEach(p => {
            const parts = participantsMap[p.id] || [];
            if (parts.length === 0) return;

            // Sort participants by chest number
            const sortedParts = [...parts].sort((a, b) => {
                const chestA = parseInt(a.chestNumber, 10);
                const chestB = parseInt(b.chestNumber, 10);
                if (!isNaN(chestA) && !isNaN(chestB)) return chestA - chestB;
                return (a.chestNumber || '').localeCompare(b.chestNumber || '');
            });

            htmlContent += `
            <div class="${pageDivClass}" style="width:100%; box-sizing:border-box; margin-bottom: 2rem;">
                <div style="text-align: center; margin-bottom: 1rem;">
                    <h2 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">GREEN ROOM SIGNING</h2>
                    <h3 style="margin: 0; font-size: 1rem; color: #475569;">${window.escapeHTML ? window.escapeHTML(p.programName || '') : p.programName}</h3>
                    <div style="font-size: 0.85rem; margin-top: 0.25rem; color: #64748b;">
                        Category: ${window.escapeHTML ? window.escapeHTML(cat.categoryName || '') : cat.categoryName}
                    </div>
                </div>
                <table class="report-table" style="width:100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="width: 50px;">SL</th>
                            <th style="width: 80px;">CHEST NO</th>
                            <th>NAME</th>
                            <th style="width: 150px;">TEAM</th>
                            <th style="width: 150px;">SIGNATURE</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            let sl = 1;
            sortedParts.forEach(part => {
                if (part.isGroup) {
                    htmlContent += `
                        <tr>
                            <td style="text-align:center;">${sl++}</td>
                            <td style="text-align:center;">${window.escapeHTML ? window.escapeHTML(part.chestNumber || '') : (part.chestNumber || '')}</td>
                            <td>
                                <strong>${window.escapeHTML ? window.escapeHTML(part.name || part.teamName || 'Group') : (part.name || part.teamName || 'Group')}</strong>
                            </td>
                            <td>${window.escapeHTML ? window.escapeHTML(part.teamName || 'Independent') : (part.teamName || 'Independent')}</td>
                            <td></td>
                        </tr>
                    `;
                } else {
                    htmlContent += `
                        <tr>
                            <td style="text-align:center;">${sl++}</td>
                            <td style="text-align:center;">${window.escapeHTML ? window.escapeHTML(part.chestNumber || '') : (part.chestNumber || '')}</td>
                            <td>${window.escapeHTML ? window.escapeHTML(part.name || part.studentName || '') : (part.name || part.studentName || '')}</td>
                            <td>${window.escapeHTML ? window.escapeHTML(part.teamName || 'Independent') : (part.teamName || 'Independent')}</td>
                            <td></td>
                        </tr>
                    `;
                }
            });

            htmlContent += `
                    </tbody>
                </table>
                <div style="margin-top: 1.5rem; text-align: right; padding-right: 2rem;">
                    <span style="font-size: 0.85rem; color: #475569;">Authorized Signature: _______________________</span>
                </div>
            </div>`;
        });
    });

    if (htmlContent === '') {
        htmlContent = `<div style="text-align:center; padding: 2rem; color: #64748b;">No participants found for Green Room Signing based on current filters.</div>`;
    }

    return htmlContent;
}

export function generateGreenRoomCSV(f, programs, participantsMap) {
    let csv = "CATEGORY,PROGRAM,CHEST NUMBER,NAME,TEAM,SIGNATURE\n";
    
    // Group programs by Category
    const groups = {};
    programs.forEach(p => {
        const catId = p.categoryId || 'unknown';
        if (!groups[catId]) {
            groups[catId] = {
                categoryName: p.categoryName || 'General',
                programs: []
            };
        }
        groups[catId].programs.push(p);
    });

    const sortedCatIds = Object.keys(groups).sort((a, b) => {
        return groups[a].categoryName.localeCompare(groups[b].categoryName);
    });

    sortedCatIds.forEach(catId => {
        const cat = groups[catId];
        const sortedPrograms = cat.programs.sort((a, b) => {
            return (a.programName || '').localeCompare(b.programName || '');
        });

        sortedPrograms.forEach(p => {
            const parts = participantsMap[p.id] || [];
            if (parts.length === 0) return;

            // Sort participants by chest number
            const sortedParts = [...parts].sort((a, b) => {
                const chestA = parseInt(a.chestNumber, 10);
                const chestB = parseInt(b.chestNumber, 10);
                if (!isNaN(chestA) && !isNaN(chestB)) return chestA - chestB;
                return (a.chestNumber || '').localeCompare(b.chestNumber || '');
            });

            sortedParts.forEach(part => {
                const catName = cat.categoryName || 'General';
                const progName = p.programName || '';
                const chest = part.chestNumber || '';
                const name = part.name || part.studentName || (part.isGroup ? 'Group' : '');
                const team = part.teamName || 'Independent';
                
                csv += `"${catName.replace(/"/g, '""')}","${progName.replace(/"/g, '""')}","${chest.replace(/"/g, '""')}","${name.replace(/"/g, '""')}","${team.replace(/"/g, '""')}",""\n`;
            });
        });
    });
    
    return csv;
}
